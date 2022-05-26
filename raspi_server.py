import socket
from motor_server import *

# TODO Information received from Raspberry Pi
RASPI_ADD: str = ""
PORT: int = 30  # 1-30, change to be consistent with device port if occupied on either device

# Assign callbacks to ultrasonic sensor
ultrasonic.when_in_range = up
ultrasonic.when_out_of_range = botOff

# Begin broadcasting the raspi's bluetooth socket and listening for connections
s: socket.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((RASPI_ADD, PORT))
s.listen(1)

# Host information
print(f"raspi_add: {RASPI_ADD} on port {PORT}")
print("Waiting for connection...")

# Accept any connections and log the address
client, address = s.accept()
print(f"Connected on address {address}")

# Begin listening for commands
while True:
    data: str = client.recv(1024).decode()
    if data == "up":
        forward()
    elif data == "down":
        backward()
    elif data == "left":
        left()
    elif data == "right":
        right()
    elif data == "stop":
        noMovement()
