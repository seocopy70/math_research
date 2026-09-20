# RESEARCH RECORDING NOTIFICATION RULE — 2026-09-20

## User-requested continuity rule

When an important research result, correction, decision, failure/closure, or next-stage transition is actually written to the authoritative GitHub research artifacts, the assistant must explicitly tell the user in the conversation that the record has been written.

The notification must distinguish:
- **기록 완료**: the artifact was successfully written/updated and the commit/result is available;
- **아직 기록 안 됨**: the assistant has discussed a result but has not successfully persisted it to the repository.

The assistant must never say “기록했다” merely because it intends to record something or because the result exists only in the chat.

This rule is operationally subordinate to RESEARCH_CONTINUITY_PROTOCOL.md and complements its immediate-recording requirement.
