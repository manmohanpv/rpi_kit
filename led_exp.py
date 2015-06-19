from time import sleep
import RPi.GPIO as GPIO

led_pin = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT, initial=GPIO.HIGH)

while True:
    GPIO.output(led_pin,GPIO.LOW)
    sleep(.1)
    GPIO.output(led_pin,GPIO.HIGH)
    sleep(.1)

GPIO.cleanup()
