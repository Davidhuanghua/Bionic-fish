# -*- coding:utf-8 -*-
import take_photo
import know_face
import uploading
import threading
import time


def A():
    
    know_face.see()
    

def B():
    
    take_photo.CatchPICFromVideo("get face", 1, 10, "./photos")


def C():
    
    uploading.up()


if __name__ == '__main__':

    print('正在载入分类器，准备人脸识别，请等待……')
    A()
    print('人脸识别已完成，准备拍照收集人脸数据，请等待……')
    time.timer = threading.Timer(21, B)
    time.timer.start()
    time.timer = threading.Timer(21, C)
    time.timer.start()
    
    
