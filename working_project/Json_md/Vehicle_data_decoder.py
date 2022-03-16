import json

class Vehicle:

    def __init__(self, r_num, y_no, passge, v_mass):
        self.r_num = r_num
        self.y_no = y_no
        self.passge = passge
        self.v_mass = v_mass


class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self, o)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)

print("what can i do for you?")
print("1. to produce a JSON string des a vehicle")
print("2. decode a JSON string into vehicle data")
answer = ""
while answer not in ['1', '2']:
    answer = input("Your Choice: ")
if answer == "1":
    rn = input("Registration number: ")
    yop = int(input("Year of production: "))
    psg = input("Passenger [y/n]: ").upper() == 'Y'
    mss = float(input("Vehicle mass: "))
    vehicle = Vehicle(rn, yop, psg, mss)
    print("Resulting JSON string is: ")
    print(json.dumps(vehicle, cls=MyEncoder))

else:
    json_str = input("Enter vehicle JSON string: ")
    try:
        new_car = json.loads(json_str, cls=MyDecoder)
        print(new_car.__dict__)
    except TypeError:
        print("the Json string doesn't describe a valid vehicle")
print("done")