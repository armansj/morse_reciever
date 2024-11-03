from stepmotor import Stepmotor
from machine import Pin, PWM
import time
import _thread

myStepMotor = Stepmotor(14, 15, 12, 11)

servo_pin = PWM(Pin(15))
servo_pin.freq(50)

PRESS_ANGLE = 80
UNPRESS_ANGLE = 100
def set_servo_angle(angle):
    duty = 500 + int((angle / 180) * 2000)
    servo_pin.duty_u16(int(duty * 65535 / 20000))

def press_pen():
    set_servo_angle(PRESS_ANGLE)
    time.sleep(0.05)

def lift_pen():
    set_servo_angle(UNPRESS_ANGLE)
    time.sleep(0.05)

def write_dot():
    press_pen()
    time.sleep(0.1)
    lift_pen()
    time.sleep(0.1)

def write_dash():
    press_pen()
    time.sleep(2)
    lift_pen()
    time.sleep(0.3)

def move_stepper_continuous(steps, speed):
    while True:
        myStepMotor.moveSteps(0, steps, speed)
        time.sleep(0.1)
steps = 32 * 64
speed = 2000

try:
    _thread.start_new_thread(move_stepper_continuous, (steps, speed))

    while True:
        write_dot()
        time.sleep(0.2)
        write_dash()
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program interrupted. Stopping the motors...")
    myStepMotor.stop()      lift_pen()
