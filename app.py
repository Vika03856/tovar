from flask import Flask
app = Flask(__name__)
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    # goods = [{"id":"1", "name":"Папка", "q":"20"}, {"id":"2", "name":"карандаш", "q":"10"}]
    goods = [{'name': 'Blok', 'q': 30, 'id': 1}, {'name': 'Paper Navikator', 'q': 188, 'id': 2},
     {'name': 'Diary', 'q': 15, 'id': 3}]
    page = render_template("table.html", goods2 = goods)
    return page

@app.route('/kontaks')
def kontaks():
    return 'Мой телефон 01!'
