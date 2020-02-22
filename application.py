from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    # set title and opening message
    title = "ようこそ"
    message = "Hi! this is App test page"
    return render_template('index.html', message=message, title=title)

@app.route('/bow', methods=['GET', 'POST'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        # get "name" from request form
        name = request.form['name']
        # render index.html
        return render_template('index.html',
                               name=name, title=title)
    else:
        # other case
        return redirect(url_for('index'))
