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

def correct_tovar(request):
    print(goods)

    new_tovar = {'name': request.form["item"], 'q': request.form["q"], 'id': 4}
    for i in goods:
        if i == goods['name']:
            goods.insert(goods['name'],i)

    print(goods)


def get_tovar_by_id(tovar_id):
    find_index = int(tovar_id)
    print(find_index)
    for tovar in goods:
        print(tovar["id"])
        if find_index == tovar['id']:
            return tovar

    print(goods)