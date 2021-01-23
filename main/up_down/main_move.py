# -*_ coding:utf -8 -*
import RPi.GPIO as GPIO
import time
import signal
import os
import threading
import signal
import atexit

#关闭警告
GPIO.setwarnings(False)
atexit.register(GPIO.cleanup) 
#pin1,2,3分别为内，中，外舵机；外舵机连接鱼尾
#pin4,5,6分别为上，左，右舵机；
#pin7就厉害了，是红外测距模块；

pin1 = 5
pin2 = 6
pin3 = 13
pin4 = 17
pin5 = 27
pin6 = 22
pin7 = 21

#设置模式为BCM
GPIO.setmode(GPIO.BCM)
#设置引脚输出情况，其中pin7就厉害了，是输入型的~
GPIO.setup(pin1,GPIO.OUT,initial=False)
GPIO.setup(pin2,GPIO.OUT,initial=False)
GPIO.setup(pin3,GPIO.OUT,initial=False)
GPIO.setup(pin4,GPIO.OUT,initial=False)
GPIO.setup(pin5,GPIO.OUT,initial=False)
GPIO.setup(pin6,GPIO.OUT,initial=False)
GPIO.setup(pin7,GPIO.IN)

#设置PWM引脚频率为50HZ
p = GPIO.PWM(pin1,50)
q = GPIO.PWM(pin2,50)
w = GPIO.PWM(pin3,50)
z = GPIO.PWM(pin4,50)
x = GPIO.PWM(pin5,50)
c = GPIO.PWM(pin6,50)

#设置开始时舵机位置为0度
p.start(0)
q.start(0)
w.start(0)
z.start(0)
x.start(0)
c.start(0)

time.sleep(0.5)

#定义前进函数
def go():
    x = time.time()
    while (True):
        for i in range(60,120,60):
            p.ChangeDutyCycle(2.5 + 10* i/180)
            q.ChangeDutyCycle(2.5 + 10* i/180)
            w.ChangeDutyCycle(2.5 + 10* i/180)            
            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)
            
            #舵机归中
            p.ChangeDutyCycle(0)
            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)

        for i in range(120,60,-60):
            p.ChangeDutyCycle(2.5 + 10* i/180)
            q.ChangeDutyCycle(2.5 + 10* i/180)
            w.ChangeDutyCycle(2.5 + 10* i/180)

            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)

            p.ChangeDutyCycle(0)
            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)

        y = time.time()
        if  ((y-x)>10):
            break
            
#定义向右函数，此时鱼鳍上部舵机右转
def right():
    x = time.time()
    while (True):
        for i in range(60,120,60):
            p.ChangeDutyCycle(2.5 + 10* i/180)
            time.sleep(0.3)


        for i in range(60,120,600):
            q.ChangeDutyCycle(2.5 + 10* i/180)    
            w.ChangeDutyCycle(2.5 + 10* i/180)
            z.ChangeDutyCycle(2.5 + 10* i/180)

            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)

            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)
            z.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)
        
        for i in range(120,60,-60):
            q.ChangeDutyCycle(2.5 + 10* i/180)    
            w.ChangeDutyCycle(2.5 + 10* i/180)
            z.ChangeDutyCycle(2.5 + 10* i/180)
            
            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)
            #舵机归中
            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)
            z.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)
            
        y = time.time()
        if  ((y-x)>10):
            break


# 定义向左函数，此时鱼鳍上部舵机左转
def left():
    x = time.time()
    while (True):
        for i in range(120,60,-60):
            p.ChangeDutyCycle(2.5 + 10* i/180)
            time.sleep(0.3)

        for i in range(60,120,60):
            q.ChangeDutyCycle(2.5 + 10* i/180)    
            w.ChangeDutyCycle(2.5 + 10* i/180)
            z.ChangeDutyCycle(2.5 + 10* i/180)

            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)

            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)
            z.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)

        for i in range(120,60,-60):
            q.ChangeDutyCycle(2.5 + 10* i/180)    
            w.ChangeDutyCycle(2.5 + 10* i/180)
            z.ChangeDutyCycle(2.5 + 10* i/180)

            time.sleep(0.3)
            time.sleep(0.3)
            time.sleep(0.3)
            # 舵机归中
            q.ChangeDutyCycle(0)
            w.ChangeDutyCycle(0)
            z.ChangeDutyCycle(0)

            time.sleep(0.2)
            time.sleep(0.2)
            time.sleep(0.2)
            
        y = time.time()
        if ((y-x)>10):
            break
# 容错处理


def wrong():

    if GPIO.input(pin7) == 0:
        print('直走')
        time.sleep(0.5)
        go()


# 主函数逻辑：如果遇到障碍->返回低电平，则触发向右函数
# 如果还是遇到障碍，则左转。如果以上都没有触发，则持续直行
if __name__ == '__main__':

    wrong()
    while True:
        
        if GPIO.input(pin7) == 0:
            
            print('右转')
            right()
            time.sleep(0.5)
                
            if GPIO.input(pin7) == 0:                   
                print('左转')
                left()
                time.sleep(0.5)
        else:
            
            print('直走')
            go()
           
        
        
    
  
        
