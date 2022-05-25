import socket

port = 3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TODO Remove
# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((socket.gethostname(), port))  # TODO Revert
s.listen(1)

print("Waiting for connection...")

client, address = s.accept()
print(f"Connected to {client} on address {address}")

while True:
    data = client.recv(1024)
    print(data.decode())
