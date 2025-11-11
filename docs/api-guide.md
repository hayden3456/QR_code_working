### API Endpoint: /api

This endpoint processes text inputs to generate AI prompts for image creation.

**Parameters:**
- text1 (str): First text input
- text2 (str): Second text input

**Validation:**
- The combined length of `text1` and `text2` must not exceed 200 characters. If exceeded, the API returns an error.

**Returns:** JSON response with generated image data or error message if validation fails
