from flask import Flask, render_template, request, jsonify
from gradio_client import Client
from PIL import Image
import io
from base64 import encodebytes
from langchain.llms import OpenAI 
import os
import random

import sys #this is for printing to terminal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    text1 = request.form['text1']
    text2 = request.form['text2']

    # Get API key from environment variable
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        return jsonify({'error': 'OPENAI_API_KEY environment variable not set'}), 500

    llm = OpenAI(temperature=0.7, openai_api_key=api_key) # initializes an AI model that will be used to come up with questions
    prompt = "You are helping to make ultra simple AI generated images for companys by providing a prompt that makes elegent cartoon like images that matches their brand. You should get creative and make abstract or otherwize eyecatching requests. You should NEVER include people, faces, or people in work cloths in the prompt. The company you are making the request for is in this industry: /n"
    prompt += text2
    ai_prompt = llm(prompt)
    ai_prompt += ", 8k high quilty"

    print(ai_prompt, file=sys.stderr)

    ran_num = random.random() * 100 

    client = Client("https://hjconstas-qrcode-diffusion.hf.space/")
    result = client.predict(
    "DreamShaper",	# str  in 'Model' Radio component
    text1,	# str  in 'QR Code Data' Textbox component
    ai_prompt, # str  in 'Prompt' Textbox component
    "logo, watermark, signature, text, BadDream, UnrealisticDream",	# str  in 'Negative Prompt' Textbox component
    100,	# int | float (numeric value between 10 and 400) in 'Number of Inference Steps' Slider component
    9,	# int | float (numeric value between 1 and 20) in 'Guidance Scale' Slider component
    0.17,	# int | float (numeric value between 0.0 and 1.0) in 'Controlnet Conditioning Tile' Slider component
    0.44,	# int | float (numeric value between 0.0 and 1.0) in 'Controlnet Conditioning Brightness' Slider component
    ran_num,	# int | float  in 'Seed' Number component
    api_name="/predict"
    )

    def get_response_image(pil_img):
        byte_arr = io.BytesIO()
        pil_img.save(byte_arr, format='PNG')
        encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii')
        return encoded_img

    pil_img = Image.open(result)
    encoded_img = get_response_image(pil_img)

    return jsonify({'ImageBytes': encoded_img})

if __name__ == '__main__':
    app.run(debug=True)


