from gpiozero import Motor
from time import sleep

# Pins 27 and 22
motor: Motor = Motor(27, 22)

print("Forward")
motor.forward()
sleep(5)
print("Back")
motor.backward()
sleep(5)
