from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Привет друг. Меня зовут ВИка!'

@app.route('/kontaks')
def kontaks():
    return 'Мой телефон 01!'