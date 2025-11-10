### /api

**Method:** POST

**Description:** Processes text inputs to generate an AI image.

**Parameters:**
- text1 (str): The QR code data.
- text2 (str): The industry description for generating the prompt.
- format (str, optional): The desired output image format (e.g., 'PNG', 'JPEG'). Defaults to 'PNG'.

**Returns:** JSON object containing the base64 encoded image.
