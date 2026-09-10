# Security policy

## Reporting

Do not file public issues containing credentials, customer source code, private
paths, tenant identifiers, or reproduction archives. Report suspected security
issues privately to the repository owner.

## Design boundary

FlagPassport must not retain credentials, authenticate to Atlassian, execute
scanned projects, or modify their files. Findings must use redacted labels and
classification evidence rather than copied source content.

## Supported scope

Until a release exists, this scaffold has no supported production version.
Security-relevant parser or output changes require synthetic regression tests.
