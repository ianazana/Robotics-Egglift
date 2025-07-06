from time import sleep
from machine import Pin, PWM

# Define pin numbers for four remaining servo motors
pin_base = 1
pin_elbow = 3
pin_wrist = 4
pin_gripper = 5

# Create PWM objects for four remaining servo motors
pwm_base = PWM(Pin(pin_base))
pwm_elbow = PWM(Pin(pin_elbow))
pwm_wrist = PWM(Pin(pin_wrist))
pwm_gripper = PWM(Pin(pin_gripper))

# Set the frequency to 50 Hz for all remaining servo motors
pwm_base.freq(50)
pwm_elbow.freq(50)
pwm_wrist.freq(50)
pwm_gripper.freq(50)

while True:
    # Move the base servo from 2000 to 3000 in steps of 10
    for position in range(1000, 3000, 10):
        pwm_base.duty_u16(position)
        sleep(0.01)
        
    # Move the elbow servo
    for position_elbow in range(3000, 6000, 10):
        pwm_elbow.duty_u16(position_elbow)
        sleep(0.01)
        
    # Move the gripper servo from 1000 to 3000 in steps of 10
    for position in range(1000, 5000, 20):
        pwm_gripper.duty_u16(position)
        sleep(0.01)

    # Move the elbow servo in reverse
    for position_elbow in range(6000, 3000, -10):
        pwm_elbow.duty_u16(position_elbow)
        sleep(0.01)
        
    # Move the base servo from 2000 to 3000 in steps of 10
    for position in range(3000, 1000, -10):
        pwm_base.duty_u16(position)
        sleep(0.01)
        
    # Move the elbow servo
    for position_elbow in range(3000, 5000, 10):
        pwm_elbow.duty_u16(position_elbow)
        sleep(0.01)

    # Move the wrist servo from 3000 to 1000 in steps of 10
    for position in range(5000, 1000, -20):
        pwm_wrist.duty_u16(position)
        sleep(0.01)
        
    # Move the gripper servo from 3000 to 1000 in steps of 10
    for position in range(5000, 1000, -20):
        pwm_gripper.duty_u16(position)
        sleep(0.01)
        
    # Move the wrist servo from 3000 to 1000 in steps of 10
    for position in range(1000, 5000, 20):
        pwm_wrist.duty_u16(position)
        sleep(0.01)    

    # Move the elbow servo in reverse
    for position_elbow in range(5000, 3000, -10):
        pwm_elbow.duty_u16(position_elbow)
        sleep(0.01)