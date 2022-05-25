from gpiozero import Motor, DistanceSensor

# TODO Forward should turns the motor COUNTER-CLOCKWISE
LMOTORA: str = "GPIO27"
LMOTORB: str = "GPIO22"

RMOTORA: str = "GPIO23"
RMOTORB: str = "GPIO24"

BMOTORA: str = "GPIO5"
BMOTORB: str = "GPIO6"

""" Connect the GND pin of the sensor to a ground pin on the Pi.
Connect the TRIG pin of the sensor a GPIO pin.
Connect one end of a 330Ω resistor to the ECHO pin of the sensor.
Connect one end of a 470Ω resistor to the GND pin of the sensor.
Connect the free ends of both resistors to another GPIO pin. This forms the required voltage divider.
Finally, connect the VCC pin of the sensor to a 5V pin on the Pi. """

TRIG = "GPIO13"
ECHO = "GPIO26"
THRESH = 1  # Meters

# Labelled when looking from "behind" (rotors facing towards you)
left_motor: Motor = Motor(LMOTORA, LMOTORB)
right_motor: Motor = Motor(RMOTORA, RMOTORB)
bot_motor: Motor = Motor(BMOTORA, BMOTORB)

ultrasonic: DistanceSensor = DistanceSensor(trigger=TRIG, echo=ECHO, threshold_distance=THRESH)


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
