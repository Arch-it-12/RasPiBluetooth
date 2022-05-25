import socket
import sys
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

# from motor import left_motor, right_motor, bot_motor, ultrasonic, forward, backward, up, down, left, right, noMovement, \
#     botOff

# ultrasonic.when_in_range = up
# ultrasonic.when_out_of_range = botOff

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
    data = client.recv(1024).decode()
    print(data)
    if data == "up":
        ...
        # forward()
    elif data == "down":
        ...
        # backward()
    elif data == "left":
        ...
        # left()
    elif data == "right":
        ...
        # right()
    elif data == "stop":
        ...
        # noMovement()
