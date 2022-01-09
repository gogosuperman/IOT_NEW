import RPi.GPIO as GPIO
import time

def switch():
    led_pin = 26
    GPIO.setmode(GPIO.BCM)

#let power to bread
    GPIO.setup(led_pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)

    while True:
        input_state = GPIO.input(led_pin)
        if input_state == False:
            print('button pressed')
            time.sleep(0.2)
    return