## Error Handling for API Key Validation

When an invalid API key length is detected, the API will respond with a 400 HTTP status code. The response will include a JSON object with an `error` field containing the message "Invalid OPENAI_API_KEY length". This immediate feedback helps users correct their API key configuration promptly.
