import requests

# ALL thge responses of HTTP are gathered here.
# for code in requests.codes.__dict__:
#     print(code,"=",requests.codes.__dict__[code])

# print(requests.codes.__dict__)

"""
Connection Error
"""
try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('wrong host')
else:
    print('Everything is fine!')

    
"""
Time Out exception
"""
try:
    reply = requests.get("http://localhost:3000", timeout=1)
except requests.exceptions.Timeout:
    print('Didn\'t get yout data')
else:
    print("Here is your data.")

# print(reply.status_code)
# print(reply.headers)
# print(reply.headers['Content-Type'])
# print(reply.text)