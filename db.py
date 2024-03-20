goods = [
    {'name': 'Blok', 'q': 30, 'id': 1},
    {'name': 'Paper Navikator', 'q': 188, 'id': 2},
    {'name': 'Diary', 'q': 15, 'id': 3}
]

def add_tovar(request):
    print(goods)
    fresh_tovar = {'name': request.form["item"], 'q': request.form["q"], 'id': 4}
    goods.append(fresh_tovar)
    print(goods)

def correc_tovar(request):
    print(goods)
    new_tovar = {'name': request.form["item"], 'q': request.form["q"], 'id': 4}
    for i in goods:
        if i == goods['name']:
            goods.insert(goods['name'],i)

   
    print(goods)