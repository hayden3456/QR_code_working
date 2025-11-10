### /api

This endpoint processes the input text and returns an AI-generated image based on the provided prompt.

**Parameters:**
- text1 (str): QR Code Data
- text2 (str): Industry description for prompt generation

**Returns:** JSON object containing base64 encoded image or an error message

**Error Handling:**
- If the `OPENAI_API_KEY` environment variable is not set, a 500 error with a message `'OPENAI_API_KEY environment variable not set'` is returned.
- If the API request fails, a 500 error with a message `'Failed to make API request'` is returned.
- If there is an error processing the generated image, a 500 error with a message `'Failed to process generated image'` is returned.
