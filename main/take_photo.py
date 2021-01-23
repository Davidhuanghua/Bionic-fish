#-*- coding: utf-8 -*-

import cv2

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    #打开摄像头
    cap = cv2.VideoCapture(0)

    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

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

if __name__ == '__main__':
    # 连续截50张图像，存进phots文件夹中
    CatchPICFromVideo("get face", 1, 100, "./photos")
    
 
    
