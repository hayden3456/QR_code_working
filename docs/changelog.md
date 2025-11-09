# Changelog

## Unreleased
- Added input validation to `/api` requiring `text1` and `text2`; returns `400 Bad Request` with `{ "error": "Both text1 and text2 inputs are required" }` when either is missing.
- Clarified error responses:
  - `500` when `OPENAI_API_KEY` is not set.
  - `500` when generated image processing fails.
