# -*- coding:utf-8 -*-
import face_recognition
import cv2
import os
import time
import take_photo
import requests

def see():
# 打开摄像头
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('拍摄记录.mp4', fourcc, 20.0, (640,480))

    # 导入人脸
    m1_image = face_recognition.load_image_file("david.jpg")
    m1_face_encoding = face_recognition.face_encodings(m1_image)[0]


    face_locations = []
    face_encodings = []

    face_names = []
    process_this_frame = True
    a = time.time()
    while True:
        
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        if process_this_frame:
            # 识别出画面中所有人脸
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            faces_to_compare = [m1_face_encoding]    

            for face_encoding in face_encodings:
                
                # 若识别出的人脸不满足结果则备注unknown
                match = face_recognition.compare_faces(faces_to_compare, face_encoding, tolerance=0.5)
                name = "Unknown"
                print(match)
                
                if match[0]:
                    name = "administrator"    #此为管理员
                
                face_names.append(name)

        process_this_frame = not process_this_frame
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 设置人脸大小
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # 框出人脸
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 4)

            # 在人脸下备注
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # 显示画面
        cv2.resizeWindow('监视画面', 600, 450)
        cv2.imshow('监视画面', frame)

        b = time.time()
        if ((b-a)>20):
            break
        # 按q退出程序。
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # 清空数据，关闭所有窗口；
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print('video close successfully ')

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    #打开摄像头
    cap = cv2.VideoCapture(0)

    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    #识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read() #读取一帧数据
        if not ok:
            print('异常退出，摄像头未开启！')
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #将当前桢图像转换成灰度图像

        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 5, minSize = (32, 32))
        if len(faceRects) > 0:          #大于0则检测到人脸
            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect

                #将当前帧保存为图片
                img_name = ("%s/%d.jpg" % (path_name, num))
                #print(img_name)
                image = frame[y - 20: y + h + 20, x - 20: x + w + 20]
                cv2.imwrite(img_name, image,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])

                num += 1
                if num > (catch_pic_num):   #如果超过指定最大保存数量退出循环
                    break

                #画出矩形框
                cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), color, 2)

                #显示当前捕捉到的人脸图片数量
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'num:%d/10' % (num),(x + 30, y + 30), font, 1, (255,0,0),4)

                #超过指定最大保存数量结束程序
        if num > (catch_pic_num):
            print('收集图像完成！')
            break

        #显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            print('成功退出拍摄！')
            break

    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()

def up():
    
    url = "http://api.heclouds.com/bindata"

    headers = {
        "Content-Type": "image/jpg", # 
        "api-key": "6XdM1tqZ9xw2cWms=AZa9U=TDBU=", # API-key（在产品概况）
    }

    # device_id是你的设备id（在设备管理）
    # datastream_id是你的数据流名称（在数据流模板）
    querystring = {"device_id": "38964809", "datastream_id": "88888888"}

    # 流式上传
    with open('./photos/3.jpg', 'rb') as f:
        requests.post(url, params=querystring, headers=headers, data=f)

    print('success')
    
  
if __name__=='__main__':
    print('正在载入分类器，准备人脸识别，请等待……')
    see()
    # 连续截50张图像，存进phots文件夹中
    print('人脸识别已完成，准备拍照收集人脸数据，请等待……')
    CatchPICFromVideo("get face", 1, 10, "./photos")
    up()
