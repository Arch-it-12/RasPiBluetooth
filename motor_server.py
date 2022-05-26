from gpiozero import Motor, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

LMOTORA: str = "GPIO27"
LMOTORB: str = "GPIO22"

RMOTORA: str = "GPIO23"
RMOTORB: str = "GPIO24"

BMOTORA: str = "GPIO5"
BMOTORB: str = "GPIO6"

TRIG: str = "GPIO13"
ECHO: str = "GPIO26"
THRESH: int = 1  # Meters

left_motor: Motor = Motor(LMOTORA, LMOTORB)
right_motor: Motor = Motor(RMOTORA, RMOTORB)
bot_motor: Motor = Motor(BMOTORA, BMOTORB)

ultrasonic: DistanceSensor = DistanceSensor(trigger=TRIG, echo=ECHO, threshold_distance=THRESH,
                                            pin_factory=PiGPIOFactory())


def forward() -> None:
    left_motor.forward()
    right_motor.forward()


def backward() -> None:
    left_motor.backward()
    right_motor.backward()


def left() -> None:
    left_motor.backward()
    right_motor.forward()


def right() -> None:
    left_motor.forward()
    right_motor.backward()


def noMovement() -> None:
    left_motor.stop()
    right_motor.stop()


def up() -> None:
    bot_motor.forward()


def down() -> None:
    bot_motor.backward()


def botOff() -> None:
    bot_motor.stop()
