from flask import Flask, render_template, request, jsonify
from gradio_client import Client
from PIL import Image
import io
from base64 import encodebytes
from langchain.llms import OpenAI 
import os
import random
import logging
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

def is_valid_url_format(url_string):
    """Validate if the input string is a valid URL format."""
    try:
        result = urlparse(url_string)
        # Check if it has at least a scheme or netloc
        # For QR codes, we accept any string, but prefer valid URLs
        return all([result.scheme, result.netloc]) or len(url_string.strip()) > 0
    except Exception:
        return len(url_string.strip()) > 0

def encode_image_to_base64(pil_img):
    """Convert PIL Image to base64 encoded string."""
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG')
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')
    return encoded_img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def generate_qr_code():
    try:
        # Validate request has required fields
        if 'text1' not in request.form or 'text2' not in request.form:
            logger.warning("Missing required form fields")
            return jsonify({'error': 'Missing required fields: text1 (URL) and text2 (Industry) are required'}), 400
        
        qr_code_data = request.form['text1'].strip()
        industry_description = request.form['text2'].strip()
        
        # Validate inputs are not empty
        if not qr_code_data:
            logger.warning("Empty URL field")
            return jsonify({'error': 'URL field cannot be empty'}), 400
        
        if not industry_description:
            logger.warning("Empty Industry field")
            return jsonify({'error': 'Industry field cannot be empty'}), 400
        
        # Validate URL format (basic validation - QR codes can contain any text)
        if not is_valid_url_format(qr_code_data):
            logger.warning(f"Invalid URL format: {qr_code_data}")
            # Note: We still allow it since QR codes can encode any text
        
        # Validate industry field length
        if len(industry_description) > 200:
            logger.warning("Industry field too long")
            return jsonify({'error': 'Industry field must be 200 characters or less'}), 400

        # Get API key from environment variable
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            logger.error("OPENAI_API_KEY not set")
            return jsonify({'error': 'OPENAI_API_KEY environment variable not set'}), 500

        logger.info(f"Generating QR code for URL: {qr_code_data[:50]}... in industry: {industry_description}")
        
        # Generate AI prompt
        llm = OpenAI(temperature=0.7, openai_api_key=api_key)
        prompt = "You are helping to make ultra simple AI generated images for companies by providing a prompt that makes elegant cartoon like images that matches their brand. You should get creative and make abstract or otherwise eye-catching requests. You should NEVER include people, faces, or people in work clothes in the prompt. The company you are making the request for is in this industry: \n"
        prompt += industry_description
        
        try:
            ai_prompt = llm(prompt)
            ai_prompt += ", 8k high quality"
            logger.info(f"Generated AI prompt: {ai_prompt[:100]}...")
        except Exception as e:
            logger.error(f"Error generating AI prompt: {e}")
            return jsonify({'error': 'Failed to generate AI prompt. Please check your OpenAI API key and try again.'}), 500

        generation_seed = int(random.random() * 100)  # Generate integer seed for reproducibility 
        logger.info(f"Using seed: {generation_seed}")

        # Generate QR code image
        try:
            client = Client("https://hjconstas-qrcode-diffusion.hf.space/")
            result = client.predict(
                "DreamShaper",	# str  in 'Model' Radio component
                qr_code_data,	# str  in 'QR Code Data' Textbox component
                ai_prompt, # str  in 'Prompt' Textbox component
                "logo, watermark, signature, text, BadDream, UnrealisticDream",	# str  in 'Negative Prompt' Textbox component
                100,	# int | float (numeric value between 10 and 400) in 'Number of Inference Steps' Slider component
                9,	# int | float (numeric value between 1 and 20) in 'Guidance Scale' Slider component
                0.17,	# int | float (numeric value between 0.0 and 1.0) in 'Controlnet Conditioning Tile' Slider component
                0.44,	# int | float (numeric value between 0.0 and 1.0) in 'Controlnet Conditioning Brightness' Slider component
                generation_seed,	# int | float  in 'Seed' Number component
                api_name="/predict"
            )
        except Exception as e:
            logger.error(f"Error calling Gradio client: {e}")
            return jsonify({'error': 'Failed to generate QR code image. The image generation service may be unavailable. Please try again later.'}), 500

        # Process and encode image
        try:
            pil_img = Image.open(result)
            encoded_img = encode_image_to_base64(pil_img)
            logger.info("Successfully generated and encoded QR code image")
            return jsonify({'ImageBytes': encoded_img})
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            return jsonify({'error': 'Failed to process generated image. Please try again.'}), 500
            
    except Exception as e:
        logger.error(f"Unexpected error in API endpoint: {e}", exc_info=True)
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    app.run(debug=True)


