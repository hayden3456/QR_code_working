# Configuration

The application requires an OpenAI API key to generate prompts.

## Environment Variables
- `OPENAI_API_KEY` (required): Your OpenAI API key.

Example (Unix):
```bash
export OPENAI_API_KEY="sk-..."
python main.py
```

If `OPENAI_API_KEY` is not set, the `/api` endpoint responds with:
```json
{ "error": "OPENAI_API_KEY environment variable not set" }
```
and HTTP status `500`.
