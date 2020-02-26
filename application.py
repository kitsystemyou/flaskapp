from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image
import numpy as np
from rq import Queue
from worker import conn
import pickle

# SAVE_DIR = "./static/images"
# SAVE_AUDIO = "/app/static/audio" # for heroku
# print(__file__)
print(os.path.dirname(__file__))
flask_root = os.path.dirname(__file__)

q = Queue(connection=conn)


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
        print("name:" + name)
        # rawaudio = request.files['uploadFile']
        # savepath = "/tmp/" + name + ".mp3"
        # rawaudio.save(savepath)
        # print(os.path.exists(savepath))
        
        # print("save:" + savepath)

        # os.system('python -m spleeter separate -i ' + savepath + ' -p spleeter:2stems -o /app/static/audio/')
        q.enqueue(background_process, name)
        
        return render_template('./result.html', title='Audio separation', name=name)
    
    else:
        return redirect(url_for('index'))

def background_process(rawaudio, name):
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
