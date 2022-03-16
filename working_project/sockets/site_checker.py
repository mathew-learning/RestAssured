import sys
import socket

if len(sys.argv) not in [2, 3]:
    print("Improper number of arguments")
print(sys.argv)
if len(sys.argv) == 3:
    try:
        port = int(sys.argv[2])
        if not (1 <= port >= 65535):
            raise ValueError
    except ValueError:
        print("Port number Not Valid")
        exit(1)
else:
    port = 80



# Write your code here.
server_addr = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((server_addr, port))
except socket.error:
    print(socket.error)
else:
    print("success")

request = b"HEAD / HTTP/1.0\r\nHost:" + \
          bytes(server_addr, "utf8") + \
          b"\r\nConnection:close\r\n\r\n"

sock.send(request)
answer = sock.recv(100).decode("utf8")
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(answer[:answer.find('\r')])

