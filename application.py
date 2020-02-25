from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image
import numpy as np


# SAVE_DIR = "./static/images"
# SAVE_AUDIO = "/app/static/audio" # for heroku
# print(__file__)
print(os.path.dirname(__file__))
SAVE_AUDIO = __file__

# if not os.path.isdir(SAVE_DIR):
#     os.mkdir(SAVE_DIR)

# if not os.path.isdir(SAVE_AUDIO):
#     os.mkdir (SAVE_AUDIO)

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
        print(name)
        rawaudio = request.files['uploadFile']
        savepath = SAVE_AUDIO + "/static/audio/" + name + ".mp3"
        rawaudio.save(savepath)
        print("get sound")
        print("save:" + savepath)

        # /home/site/wwrot is an azure directory
        os.system('python -m spleeter separate -i ' + savepath + ' -p spleeter:2stems -o /app/static/audio/')
        print("static/audio/" + name)
        return render_template('./result.html', title='Audio separation', name=name)
    
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000), debug=None)
