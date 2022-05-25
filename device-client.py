import keyboard as kb
import socket
import sys

raspi_add = sys.argv[1]
port = 30 if len(sys.argv) <= 2 else int(sys.argv[2])

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
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
    if e.name in ("up", "down", "left", "right") and e.name == state:
        state = "stop"
        s.send("stop".encode())


kb.on_press_key("left", left)
kb.on_press_key("right", right)
kb.on_press_key("up", up)
kb.on_press_key("down", down)

kb.on_release(stop)

kb.wait()
