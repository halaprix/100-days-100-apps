## Summary

- What changed?
- Which supported configuration shape or safety rule does it affect?

## Validation

- [ ] `python3 scripts/verify_scaffold.py`
- [ ] Relevant fixture tests
- [ ] No real configurations, tokens, headers, or local paths included

## Safety boundary

- [ ] No network, authentication, browser, or automatic file-edit behavior added
- [ ] Ambiguous input remains explicit rather than inferred
