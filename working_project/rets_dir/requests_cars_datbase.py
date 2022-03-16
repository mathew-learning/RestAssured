import json
import requests

key_header = ['id', 'brand', 'model', 'production_year', 'convertible']
key_width = [10, 15, 10, 20, 15]


def show_head():
    for (n, w) in zip(key_header, key_width):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_width:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_header, key_width):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


h_close = {'Connection': 'Close'}
h_content = {'Content-Type' : 'application/json'}
new_car = {'id': 6,
           'brand': 'Mercedes Benz',
           'model': '300SL',
           'production_year': 1967,
           'convertible': False}
print(json.dumps(new_car))

try:
    reply = requests.put("http://localhost:3000/cars/6", headers=h_content, data=json.dumps(new_car))
    print("res=" + str(reply.status_code))
    reply = requests.get('http://localhost:3000/cars/', headers=h_close)
except requests.RequestException:
    print("Communication error")
else:
    print('Connection=' + reply.headers['Connection'])
    if reply.status_code == requests.codes.ok:
        show(reply.json())
    elif reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print("Server error")
