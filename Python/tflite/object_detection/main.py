import RPi.GPIO as GPIO
import time
import server_motor
import dc_motor
import text_to_speach 
import redis

r = redis.Redis(host='localhost',port = 6379)
led_pin = 22
GPIO.setmode(GPIO.BCM)

#let power to bread
GPIO.setup(led_pin,GPIO.OUT)
servol = GPIO.PWM(led_pin,50)
servol.start(0)

print('rotate 360 degrees')

while True:
    label = 'no' if r.get('label') == None else r.get('label').decode()
    print(label)
    if label =='person':
        break
    servol.ChangeDutyCycle(3)
    time.sleep(1.4)
print('1')
text_to_speach.text_to_speach()
#dc_motor.dc_motor()
server_motor.server_motor()
dc_motor.dc_motor()
'''
server_motor_buttom.server_motor_buttom
if TFLite_detection_webcam == 'person':
    stop server_motor_buttom

server_motor_buttom.server_motor_buttom
server_motor.server_motor
dc_motor.dc_motor
text_to_speach.text_to_speach('RESULT FROM FRONT END')
'''