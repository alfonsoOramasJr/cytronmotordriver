import time
from MotorDriver import MotorDriver

PWM_PINOUT = 18
DIRECTIONAL_PINOUT = 17

motor_controller = MotorDriver(PWM_PINOUT, DIRECTIONAL_PINOUT, 12000) ## 12,000Khz frequency

## Forwards direction at 10% of its duty cycle.
motor_controller.set_motor_speed(10)
time.sleep(2)

## Stops the motor.
motor_controller.set_motor_speed(0)
time.sleep(2)

## Backwards direction at 10% of its duty cycle.
motor_controller.set_motor_speed(-10)
time.sleep(2)

motor_controller.set_motor_speed(0)
time.sleep(2)

motor_controller.cleanup()