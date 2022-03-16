"""
json.dumps
json.loads
"""
import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, z)

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__+'is not JSON serializable')

def decode_who(w):
    return Who(w['name'], w['age'])

some_man = Who('matthew', 29)
# json_str = json.dumps(some_man, default=encode_who)
json_str = json.dumps(some_man, cls=MyEncoder)
know_man = json.loads(json_str, cls=MyDecoder)
# know_man = json.loads(json_str, object_hook=decode_who)
print(type(know_man))
print(know_man.__dict__)


electron = 1.60217662089E10-19
comics = "'the meaning of life' by monty python\'s flying circus"

json_dta = json.dumps(comics)
# print(json_dta)
# comics_str = json.loads(json_dta)
# print(type(comics_str))
# print(comics_str)




