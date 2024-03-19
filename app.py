from flask import Flask, request,render_template,redirect
from db import goods, add_tovar
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    page = render_template("table.html", goods2 = goods)
    return page

@app.route('/create',methods=["GET","POST"])
def create():
    if request.method =='POST':
        add_tovar(request)
        return redirect("/")
    else:
        return render_template("create.html")
