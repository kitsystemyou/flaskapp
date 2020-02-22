from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image
import numpy as np


SAVE_DIR = "./static/images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

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
    # exist or not uploaded file
    if request.files['uploadFile']:
        file_uploaded = request.files['uploadFile']
        # get filename without extention
        name = os.path.splitext(file_uploaded.filename)[0]
        # read as RGB image
        image_pil = Image.open(request.files['uploadFile']).convert('RGB')
        image = np.array(image_pil, 'uint8')
        print("success reading image")
        predict_Confidence = 1
        lenimage = len(image[0])
        # save image
        savepath = SAVE_DIR + "/" + name +".png"
        image_pil.save(savepath)
        print("get image")
        return render_template('./result.html', title='類似度', savepath=savepath)
    
    else:
        return redirect(url_for('index'))


