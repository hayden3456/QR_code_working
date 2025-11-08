# QR Code Generator with AI-Generated Images

A Flask web application that generates QR codes with AI-generated artistic designs based on company industry information.

## Features

- Generate QR codes with custom URLs
- AI-powered image generation based on industry type
- Elegant cartoon-like designs that match brand aesthetics
- Download generated QR code images

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export OPENAI_API_KEY=your_api_key_here
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Enter a URL in the "URL" field
2. Enter the industry type in the "Industry" field
3. Click "Submit" to generate your QR code
4. Use "Redo" to generate a new variation
5. Use "Download" to save the image

## Technologies

- Flask - Web framework
- OpenAI (LangChain) - AI prompt generation
- Gradio Client - Image generation
- PIL/Pillow - Image processing

