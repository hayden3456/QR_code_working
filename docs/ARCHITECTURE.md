# Architecture Overview

## System Components

### 1. Flask Web Application (`main.py`)
- **Framework:** Flask
- **Purpose:** Handles HTTP requests and serves the web interface
- **Routes:**
  - `/` - Main page
  - `/api` - QR code generation endpoint

### 2. AI Prompt Generation
- **Service:** OpenAI (via LangChain)
- **Purpose:** Generates creative image prompts based on industry type
- **Model:** Uses OpenAI's language model with temperature 0.7

### 3. Image Generation
- **Service:** Gradio Client
- **Endpoint:** `https://hjconstas-qrcode-diffusion.hf.space/`
- **Model:** DreamShaper
- **Purpose:** Generates artistic QR code images

### 4. Image Processing
- **Library:** PIL/Pillow
- **Purpose:** Processes and encodes generated images to base64

## Workflow

1. User submits URL and industry type via web form
2. Flask receives POST request at `/api`
3. OpenAI generates a creative image prompt based on industry
4. Gradio client generates QR code image with artistic design
5. Image is processed and encoded to base64
6. Base64 image is returned to client as JSON

## Dependencies

- **Flask** - Web framework
- **gradio-client** - Interface with Gradio API
- **Pillow** - Image processing
- **langchain** - AI/LLM integration
- **openai** - OpenAI API client

