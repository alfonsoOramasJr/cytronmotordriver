# Cytron Board Layout
![alt text](<README IMAGES/Board Layout.png>)

Connect the PWM pin from the raspberry pi to the PWM pin on the board (Pin No. 2), the Directional Pin (Pin No. 3), and finally the ground pin (Pin No.1).

To get the example up and running ASAP, the following pins on the raspberry pi are highlighted in the image below.

* GPIO 18 **(PWM PIN)**
* GPIO 17 **(DIRECTIONAL PIN)**

![alt text](<README IMAGES/Raspberry Pi Pinouts.png>)

# Using the MotorDriver Class

Choosing the direction of which way the motor rotates to is decided by sending a HIGH or LOW signal to the board's direction pin.

| DIRECTIONAL PIN | MOTOR DIRECTION |
|-----------------|-----------------|
|             LOW |        Backward |
|            HIGH |         Forward |

```python
from time import sleep
from MotorDriver import MotorDriver

PWM_PINOUT = 18
DIRECTIONAL_PINOUT = 17

motor_controller = MotorDriver(PWM_PINOUT, DIRECTIONAL_PINOUT)

## The motor moves forward at 10% of its speed.
motor_controller.set_motor_speed(10)
sleep(2)

## Motor stops.
motor_controller.set_motor_speed(0)
sleep(2)

## Motor moves backwards at 10% of its speed.
motor_controller.set_motor_speed(-10)
sleep(2)

## Motor gracefully shuts down, and cleans up the GPIO.
motor_controller.set_motor_speed(0)
motor_controller.cleanup()
```