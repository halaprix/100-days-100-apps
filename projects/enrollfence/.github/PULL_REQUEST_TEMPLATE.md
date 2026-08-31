## Summary

- What changed?
- Why is it needed?

## Safety boundary

- [ ] No credentials, real tenant exports, device/user identifiers, or raw
      configuration contents are introduced.
- [ ] The change stays local and read-only.
- [ ] Unknown conditions are not represented as policy guarantees.

## Verification

- [ ] `python3 scripts/verify_scaffold.py`
- [ ] `git diff --check`
