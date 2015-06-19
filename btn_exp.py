import RPi.GPIO as GPIO
from time import sleep

led_pin = 11
btn_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    GPIO.output(led_pin, GPIO.HIGH)
    while GPIO.input(btn_pin) == GPIO.LOW:
        GPIO.output(led_pin, GPIO.LOW)
        sleep(.1)
        GPIO.output(led_pin, GPIO.HIGH)
        sleep(.1)


GPIO.cleanup()
