#!/usr/bin/env bash
set -euo pipefail

# Install GAP from Ubuntu and build a pinned ANUPQ release.
# Ubuntu 24.04 (noble), used by ubuntu-latest, does not ship gap-anupq;
# therefore ANUPQ must be installed from the upstream GAP package release.

ANUPQ_VERSION="3.3.3"
ANUPQ_TAG="v${ANUPQ_VERSION}"
ANUPQ_COMMIT="9d0ac7dea81e22f5adde32e7e319d05a1e634db7"
GAP_ROOT="/usr/share/gap"
ANUPQ_DIR="${GAP_ROOT}/pkg/anupq"

sudo apt-get update
sudo apt-get install -y gap gap-autpgrp git build-essential

# Do not rely on a distro gap-anupq package: it is absent from Ubuntu noble.
sudo rm -rf "${ANUPQ_DIR}"
sudo git clone --depth 1 --branch "${ANUPQ_TAG}" https://github.com/gap-packages/anupq.git "${ANUPQ_DIR}"

actual_commit="$(git -C "${ANUPQ_DIR}" rev-parse HEAD)"
test "${actual_commit}" = "${ANUPQ_COMMIT}"

cd "${ANUPQ_DIR}"
sudo ./configure --with-gaproot="${GAP_ROOT}"
sudo make

# Fail here, before the solver, unless GAP can actually load the package.
gap -q <<'GAP'
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ANUPQ_LOAD=", LoadPackage("anupq"), "\n");
if not IsPackageLoaded("anupq") then
  Error("ANUPQ package could not be loaded");
fi;
QUIT;
GAP
