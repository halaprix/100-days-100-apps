#!/usr/bin/env bash
set -euo pipefail

# Remove the former dedicated GitHub repos after their snapshots are pushed in
# halaprix/100-days-100-apps. Dry-run by default.
#
# Usage:
#   scripts/remove-dedicated-github-repos.sh
#   CONFIRM_DELETE_100_DAYS_REPOS=yes scripts/remove-dedicated-github-repos.sh --execute
#
# Requirements:
#   - GITHUB_TOKEN with Administration/write access to the target repos
#   - curl
#
# This script intentionally never touches halaprix/100-days-100-apps.

OWNER="halaprix"
MODE="dry-run"
if [[ "${1:-}" == "--execute" ]]; then
  MODE="execute"
fi

REPOS=(
  'backup-locksmith'
  'baytrace'
  'become-doctor'
  'campaignpacket'
  'comment-pulse'
  'davsync-doctor'
  'deskpatch'
  'exittrace'
  'free-tier-fit'
  'headerpass'
  'labfit'
  'llama-cuda-doctor'
  'mxcutover'
  'nis2-evidencepack'
  'oobeguard'
  'peerpath'
  'pipe-twin'
  'portlease'
  'proxyenv-doctor'
  'querygap'
  'r2-backup-probe'
  'replayfence'
  'reportchain'
  'sheetsentry'
  'splitpath'
  'storepacket'
  'tenant-route'
  'ticketscrub'
  'tzdrift'
  'vram-janitor'
  'winsvc-beacon'
 )

if [[ "$MODE" != "execute" ]]; then
  echo "DRY RUN: would delete ${#REPOS[@]} dedicated repos:"
  for repo in "${REPOS[@]}"; do
    echo "  ${OWNER}/${repo}"
  done
  echo
  echo "To actually delete:"
  echo "  CONFIRM_DELETE_100_DAYS_REPOS=yes $0 --execute"
  exit 0
fi

if [[ "${CONFIRM_DELETE_100_DAYS_REPOS:-}" != "yes" ]]; then
  echo "Refusing to delete. Set CONFIRM_DELETE_100_DAYS_REPOS=yes and pass --execute." >&2
  exit 2
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
  echo "GITHUB_TOKEN is required." >&2
  exit 2
fi

for repo in "${REPOS[@]}"; do
  if [[ "$repo" == "100-days-100-apps" ]]; then
    echo "Refusing to delete the master repo." >&2
    exit 3
  fi
  url="https://api.github.com/repos/${OWNER}/${repo}"
  echo "Deleting ${OWNER}/${repo} ..."
  code=$(curl -sS -o /tmp/remove-dedicated-repo-response.json -w '%{http_code}'     -X DELETE     -H "Authorization: Bearer ${GITHUB_TOKEN}"     -H "Accept: application/vnd.github+json"     -H "X-GitHub-Api-Version: 2022-11-28"     "$url")
  if [[ "$code" == "204" ]]; then
    echo "  deleted"
  else
    echo "  failed: HTTP $code" >&2
    sed -n '1,160p' /tmp/remove-dedicated-repo-response.json >&2 || true
    exit 1
  fi
done
