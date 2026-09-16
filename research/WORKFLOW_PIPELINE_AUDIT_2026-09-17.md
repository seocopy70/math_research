# Workflow Pipeline Audit — 2026-09-17

## Goal

Before continuing B1-1-2, audit the entire GitHub Actions workflow tree for shell pipelines that can fail open, with special attention to `| gap`, `| python`, `| bash`, and `| sh`.

## Method

`research/WORKFLOW_PIPELINE_AUDIT_2026-09-17.py` scans every `.yml`/`.yaml` file under `.github/workflows` and reports risky pipelines. Any matching workflow without an explicit `pipefail` setting causes CI failure.

This is an AST-independent text-level workflow audit because the target is shell syntax embedded in YAML, not Python code.

## Actual result

GitHub Actions run **35160653591**, job **105010389018**:

- workflow files scanned: **73**
- risky pipeline occurrences: **2**
- unprotected risky pipelines: **0**
- result: **PASS**

The two and only two matches are:

1. `.github/workflows/a3-4-20r-loewy-layer-alignment.yml`
   - GAP sanity probe
   - now protected by `set -euo pipefail`
   - explicit `GF(3)` matrix supplied to `GModuleByMats`

2. `.github/workflows/b1-1-w-uniseriality-test.yml`
   - GAP sanity probe
   - now protected by `set -euo pipefail`
   - explicit `GF(3)` matrix supplied to `GModuleByMats`

A3-4-20S uses a heredoc rather than a shell pipeline, so it is not affected by the specific fail-open pipeline mechanism. A3-4-18, A3-4-19, and the original A3-4-20 workflow do not contain the audited pipeline pattern.

## Historical impact assessment

The audit does **not** invalidate all historical GitHub Actions successes. It identifies exactly two workflows whose GAP sanity probe used the vulnerable pipeline pattern.

Therefore:

- historical GAP-related results from **A3-4-20R** and **B1-1** require contextual rechecking of the sanity-probe evidence before treating that probe as independently certified;
- the main mathematical computations are not automatically invalidated by this finding;
- a mathematical result becomes invalid only if the affected computation actually depended on a failed/unverified condition;
- later successful runs using the corrected workflow must be distinguished from the older fail-open runs.

## Classification

- Repository-wide audit: **PASS**
- Historical fail-open exposure: **2 workflow files**
- Automatic mathematical invalidation: **none**
- Historical sanity-probe certification: **RECHECK REQUIRED** for affected old runs

## Permanent prevention

The new CI gate `.github/workflows/workflow-pipeline-audit.yml` runs whenever workflow files or the audit script change. New risky pipelines without `pipefail` are therefore blocked before being accepted as verified infrastructure.
