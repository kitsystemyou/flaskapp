from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image
import numpy as np

app = Flask(__name__)

# @app.route("/")
# def hello():
#     print("Handling request to home page.")
#     return "Hello Azure"

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/result', methods=['POST'])
def result():
    # submitした画像が存在したら処理する
    if request.files['image']:
        # color画像として読み込み
        image_pil = Image.open(request.files['image']).convert('RGB')
        image = np.array(image_pil, 'uint8')
        print("success reading image")
        predict_Confidence = 1
        lenimage = len(image[0])

        return render_template('./result.html', title='類似度', predict_Confidence=predict_Confidence, lenimage=lenimage)
    
    else:
        return redirect(url_for('index'))

