import keyboard as kb
import socket

# TODO Information received from Raspberry Pi
RASPI_ADD = "B8:27:EB:82:E3:A9"
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
kb.on_press_key("w", move)
kb.on_press_key("a", move)
kb.on_press_key("s", move)
kb.on_press_key("d", move)

kb.on_release_key("w", stop)
kb.on_release_key("a", stop)
kb.on_release_key("s", stop)
kb.on_release_key("d", stop)


# Prevent termination
kb.wait()
