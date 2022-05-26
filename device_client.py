import keyboard as kb
import socket

# TODO Information received from Raspberry Pi
RASPI_ADD = ""
PORT = 30  # 1-30, change to be consistent with raspi port if occupied on either device
STATE = "stop"

# Connect to raspi bluetooth socket
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((RASPI_ADD, PORT))


# Define callbacks
def move(e) -> None:
    global STATE
    if STATE == "stop":
        STATE = e.name
        s.send(e.name.encode())


def stop(e) -> None:
    global STATE
    if e.name == STATE:
        STATE = "stop"
        s.send("stop".encode())


# Assign callbacks to key-presses
kb.on_press_key("left", move)
kb.on_press_key("right", move)
kb.on_press_key("up", move)
kb.on_press_key("down", move)

kb.on_release_key("left", stop)
kb.on_release_key("right", stop)
kb.on_release_key("up", stop)
kb.on_release_key("down", stop)

# Prevent termination
kb.wait()
