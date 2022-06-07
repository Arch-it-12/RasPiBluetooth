from gpiozero import Motor, DistanceSensor

LMOTORA: str = "GPIO27"
LMOTORB: str = "GPIO22"

RMOTORA: str = "GPIO23"
RMOTORB: str = "GPIO24"

BMOTORA: str = "GPIO5"
BMOTORB: str = "GPIO6"

TRIG: str = "GPIO26"
ECHO: str = "GPIO4"
THRESH: float = 0.5  # Meters

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


def no_movement() -> None:
    left_motor.stop()
    right_motor.stop()


def up() -> None:
    bot_motor.forward()


def down() -> None:
    bot_motor.backward()


def bot_off() -> None:
    bot_motor.stop()
