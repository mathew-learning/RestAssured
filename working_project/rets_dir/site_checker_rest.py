import sys
import requests

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments")
print(sys.argv)
addr = sys.argv[1]
URI = 'http://' + sys.argv[1]
if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port >= 65535):
            raise ValueError
    except ValueError:
        print("Port number Not Valid")
        exit(1)
    URI += ':' + str(port)
URI += '/'


try:
    reply = requests.head(URI)
except requests.exceptions.InvalidURL:
    print("The given URL" + sys.argv[1] + " is invalid")
    exit(2)
except requests.exceptions.ConnectionError:
    print("Cannot connect to addr")
    exit(3)
except requests.exceptions.RequestException:
    print("some problems appeared - sorry")
    exit(4)
else:
    print(reply.status_code, reply.reason)
