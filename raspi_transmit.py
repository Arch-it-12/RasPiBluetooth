import socket
import picamera
from motor_server import ultrasonic, up, left, right, forward, bot_off, no_movement

# TODO Information from Raspberry Pi
import sys

RASPI_ADD: str = "10.0.0.27"
PORT: int = 30  # 1-30, change to be consistent with device port if occupied on either device

# Begin broadcasting the raspi's bluetooth socket and listening for connections
s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((RASPI_ADD, PORT))
s.listen(1)

# Host information
print(f"raspi_add: {RASPI_ADD} on port {PORT}")
print("Waiting for connection...")

# Accept any connections and log the address
client, address = s.accept()
print(f"Connected on address {address}")

pc = picamera.PiCamera()
while True:
    frame = None
    pc.capture(frame, format="png")

    frame = bytes(frame)
    start = 0
    end = 1024
    final = len(frame)
    while end < final:
        client.send(frame[start:end])
        start = end + 1
        end += 1024
    client.send(b"Complete")

    data = client.recv(1024).decode()
    data = data.split(";")
    for i in data:
        if i == "up":
            up()
        elif i == "left":
            left()
        elif i == "right":
            right()
        elif i == "forward":
            forward()
        elif i == "nomov":
            no_movement()
        elif i == "00":
            ultrasonic.threshold = ultrasonic.distance
        elif i == "10":
            ultrasonic.when_in_range = None
            ultrasonic.when_out_of_range = None
        elif i == "11":
            ultrasonic.when_in_range = up
            ultrasonic.when_out_of_range = bot_off


