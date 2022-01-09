import RPi.GPIO as GPIO
import time

def server_motor_buttom(object_name):

    led_pin = 22
    GPIO.setmode(GPIO.BCM)

    #let power to bread
    GPIO.setup(led_pin,GPIO.OUT)
    servol = GPIO.PWM(led_pin,50)
    servol.start(0)

    print('rotate 360 degrees')

    while(object_name != 'person'):
        servol.ChangeDutyCycle(3)
        time.sleep(1.4)
        
    #servol.ChangeDutyCycle(12)
    #time.sleep(5)
        

    
    GPIO.cleanup()

