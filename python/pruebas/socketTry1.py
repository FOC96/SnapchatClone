from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Flask.render_template('main.html', name=name)
