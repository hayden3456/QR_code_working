# Changelog

## [Unreleased]
- Backend:
  - Added input validation for `text1` (URL/text) and `text2` (Industry, max 200 chars)
  - Introduced structured error responses with `error` field
  - Returned appropriate HTTP status codes (400 for validation, 500 for server issues)
  - Replaced print statements with structured logging
  - Wrapped external API calls with try/except and clearer messages
  - Refactored helper functions (`validate_url`, `get_response_image`)
- Frontend:
  - Added client-side validation and HTML5 constraints
  - Added user-facing error UI (`#errorMessage`) and detailed error messages
  - Implemented request timeout (2 minutes) and robust AJAX error handling
  - Improved redo flow using last request data
