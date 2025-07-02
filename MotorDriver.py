import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class MotorDriver:
    def __init__(self, pwm_pin, direction_pin, pwm_frequency=10000): ## 10khz pwm frequency
        GPIO.setup([pwm_pin, direction_pin], GPIO.OUT)
        self.pwm_controller = GPIO.PWM(pwm_pin, pwm_frequency)
        self.direction_pin = direction_pin
        self.pwm_controller.start(0)
    
    def forward(self, speed):
        GPIO.output(self.direction_pin, GPIO.HIGH)
        self.pwm_controller.ChangeDutyCycle(speed)

    def backward(self, speed):
        GPIO.output(self.direction_pin, GPIO.LOW)
        self.pwm_controller.ChangeDutyCycle(speed)
    
    def stop(self):
        self.pwm_controller.ChangeDutyCycle(0)
    
    def cleanup(self):
        self.stop()
        GPIO.cleanup()
    
    def set_motor_speed(self, speed):
        speed = max(-100, min(100, speed))
        if speed > 0:
            self.forward(speed)
        elif speed < 0:
            self.backward(-speed)
        else:
            self.stop()