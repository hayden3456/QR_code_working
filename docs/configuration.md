# Configuration

## Environment Variables
- `OPENAI_API_KEY` (required)
  - Used by the backend to generate the AI prompt with OpenAI.
  - If not set, the API returns `500` with `{ "error": "OPENAI_API_KEY environment variable not set" }`.

## Logging
- The application configures logging at startup:
  - Level: `INFO`
  - Format: `%(asctime)s - %(levelname)s - %(message)s`
- Logs include validation warnings, external service errors, and unexpected exceptions.

## Runtime
- Default Flask run: `app.run(debug=True)` (development mode). For production, use a WSGI server and set appropriate logging and environment variables.
