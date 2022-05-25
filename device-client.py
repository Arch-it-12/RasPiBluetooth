import keyboard as kb
import socket

raspi_add = socket.gethostname()  # TODO Revert
port = 3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TODO Remove
# s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((raspi_add, port))

state = "stop"


def left(e):
    global state
    if state == "stop":
        state = "left"
        s.send("left".encode())


def right(e):
    global state
    if state == "stop":
        state = "right"
        s.send("right".encode())


def up(e):
    global state
    if state == "stop":
        state = "up"
        s.send("up".encode())


def down(e):
    global state
    if state == "stop":
        state = "down"
        s.send("down".encode())


def stop(e):
    global state
    print("stop")
    if e.name in ("up", "down", "left", "right") and e.name == state:
        state = "stop"
        s.send("stop".encode())


kb.on_press_key("left", left)
kb.on_press_key("right", right)
kb.on_press_key("up", up)
kb.on_press_key("down", down)

kb.on_release(stop)

kb.wait()
