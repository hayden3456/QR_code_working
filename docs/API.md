# API Documentation

## Endpoints

### GET `/`
Returns the main HTML page for the QR code generator interface.

**Response:** HTML page

---

### POST `/api`
Generates a QR code with an AI-generated artistic design.

**Request Parameters:**
- `text1` (form data): The URL/data to encode in the QR code
- `text2` (form data): The industry type/description for AI image generation

**Response:**
- **Success (200):**
  ```json
  {
    "ImageBytes": "base64_encoded_image_string"
  }
  ```
- **Error (500):**
  ```json
  {
    "error": "Error message"
  }
  ```

**Common Errors:**
- `OPENAI_API_KEY environment variable not set` - Missing API key
- `Failed to process generated image` - Image processing error

**Example Request:**
```bash
curl -X POST http://localhost:5000/api \
  -F "text1=https://example.com" \
  -F "text2=Technology"
```

