from flask import Flask, request,render_template,redirect
from db import goods, add_tovar, get_tovar_by_id, correct_tovar
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
@app.route('/correction/<tovar_id>', methods=["GET","POST"])
def correction(tovar_id):
    if request.method =='POST':
        add_tovar(request)
        return redirect("/")
    else:
        finded_tovar = get_tovar_by_id(tovar_id)
        return render_template("correction.html", correct_tovar = finded_tovar)