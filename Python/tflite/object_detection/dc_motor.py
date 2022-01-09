import RPi.GPIO as GPIO
from time import sleep

def dc_motor():

    ena = 25
    in1 = 23
    in2 = 24
    enb = 13
    in3 = 5
    in4 = 6

    GPIO.setmode(GPIO.BCM)
    

    GPIO.setup(ena,GPIO.OUT)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)

    pwm = GPIO.PWM(ena,500)

    GPIO.setup(enb,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)

    pwm2 = GPIO.PWM(enb,500)
    pwm.start(50)
    GPIO.output(in1 , GPIO.LOW)
    sleep(0.1)
    GPIO.output(in2 , GPIO.HIGH)

    pwm2.start(50)
    GPIO.output(in3 , GPIO.LOW)
    sleep(0.1)
    GPIO.output(in4 , GPIO.HIGH)
    sleep(10)
    GPIO.cleanup()

'''
'''
'''



# GPIO.output(in3_forward , GPIO.HIGH) 
# sleep(5)
# GPIO.output(in3_forward , GPIO.LOW) 
# 
# GPIO.output(in2_backward , GPIO.HIGH)
# sleep(5)
# GPIO.output(in2_backward , GPIO.LOW)
# 
# 
# GPIO.output(in4_backward , GPIO.HIGH)
# sleep(5)
# 
# GPIO.output(in4_backward , GPIO.LOW)  

     
GPIO.output(in4_backward , GPIO.HIGH)
sleep(5)
GPIO.output(in4_backward , GPIO.LOW)

pwm = GPIO.PWM(in1,100)
pwm1 = GPIO.PWM(in2,100)
pwm.start(0)
pwm1.start(0)

for i in range(0,50):
    pwm.ChangeDutyCycle(i)
    sleep(2)

for i in range(50,-1,-1):
    pwm1.ChangeDutyCycle(i)
    sleep(2)
    
for j in range(0,50):
    pwm1.ChangeDutyCycle(j)
    sleep(2)

for j in range(50,-1,-1):
    pwm1.ChangeDutyCycle(j)
    sleep(2)
 
pwm.ChangeDutyCycle(0)
pwm1.ChangeDutyCycle(0)
pwm.stop()
pwm1.stop()
'''
