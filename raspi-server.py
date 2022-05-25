import socket
import sys

raspi_add = "e4:70:b8:d3:d7:c1"
port = 30 if len(sys.argv) == 1 else int(sys.argv[1])

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((raspi_add, port))
s.listen(1)

print(f"raspi_add: {raspi_add}")
print("Waiting for connection...")

client, address = s.accept()
print(f"Connected on address {address}")

while True:
    data = client.recv(1024)
    print(data.decode())
