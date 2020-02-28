from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import numpy as np
from rq import Queue
from worker import conn
import pickle

# SAVE_DIR = "./static/images"
# SAVE_AUDIO = "/app/static/audio" # for heroku
# print(__file__)
print(os.path.dirname(__file__))
flask_root = os.path.dirname(__file__)

SAVE_AUDIO = "./static/audio"
# AZURE_PATH = "/home/site/wwroot/" 

if not os.path.isdir(SAVE_AUDIO):
    os.mkdir (SAVE_AUDIO)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024

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
        savepath = SAVE_AUDIO + "/" + name + ".mp3"
        rawaudio.save(savepath)
        print("save sound")
        print(savepath)
        print("check path1:" + str(os.path.exists(savepath)))
        os.system('python -m spleeter separate -i ' + savepath +  ' -p spleeter:2stems -o ' \
                    + SAVE_AUDIO)
        print("check path2:" + str(os.path.exists(savepath)))
        print(os.path.exists("./static/audio/" + name + "/vocals.wav"))

        return render_template('./result.html', title='Audio separation', name=name)
    
    else:
        return redirect(url_for('index'))

def background_process(name):
    # print("process separation")
    # savepath = os.path.join(flask_root, savepath[1:])
    # print("savepath:" + savepath)
    rawaudio = request.files['uploadFile']
    savepath = "/tmp/" + name
    rawaudio.save(savepath)
    print("get sound")
    print(os.path.exists(savepath))
    os.system('python -m spleeter separate -i ' + savepath + ' -p spleeter:2stems -o /tmp')
    print("finish separation")

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000), debug=None)
