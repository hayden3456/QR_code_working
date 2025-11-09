# Migration Guide

## Input validation for `/api`
Behavior change: Both `text1` and `text2` are now required form fields.

- Previously: Missing fields could pass through to processing (or cause server-side errors).
- Now: If either `text1` or `text2` is missing or empty, the endpoint returns:
  - HTTP 400
  - Body: `{ "error": "Both text1 and text2 inputs are required" }`

Action required for clients:
- Ensure requests to `/api` always include non-empty `text1` and `text2` fields.
- Update client-side validation and tests accordingly.
