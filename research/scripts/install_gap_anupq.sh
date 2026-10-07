#!/usr/bin/env bash
set -euo pipefail

# Ubuntu 24.04 (noble), used by ubuntu-latest, does not ship gap-anupq.
# Install GAP/AutPGrp from Ubuntu and the pinned upstream ANUPQ release.

ANUPQ_VERSION="3.3.3"
ANUPQ_URL="https://github.com/gap-packages/anupq/releases/download/v${ANUPQ_VERSION}/anupq-${ANUPQ_VERSION}.tar.gz"
ANUPQ_SHA256="6a1b25ddcdb05abd933911f8e0e718b195d24b502e5d098d4b431db5f371ffc2"
GAP_ROOT="/usr/share/gap"
ANUPQ_DIR="${GAP_ROOT}/pkg/anupq"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

sudo apt-get update
sudo apt-get install -y gap gap-autpgrp curl build-essential

archive="${TMP_DIR}/anupq-${ANUPQ_VERSION}.tar.gz"
curl -fsSL --retry 3 "${ANUPQ_URL}" -o "${archive}"
echo "${ANUPQ_SHA256}  ${archive}" | sha256sum -c -

sudo rm -rf "${ANUPQ_DIR}"
mkdir "${TMP_DIR}/pkg"
tar -xzf "${archive}" -C "${TMP_DIR}/pkg"
topdir="$(find "${TMP_DIR}/pkg" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | head -n1)"
test -n "${topdir}"
sudo mv "${TMP_DIR}/pkg/${topdir}" "${ANUPQ_DIR}"

cd "${ANUPQ_DIR}"
sudo ./configure --with-gaproot="${GAP_ROOT}"
sudo make

gap -q <<'GAP'
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ANUPQ_LOAD=", LoadPackage("anupq"), "\n");
if not IsPackageLoaded("anupq") then
  Error("ANUPQ package could not be loaded");
fi;
QUIT;
GAP
