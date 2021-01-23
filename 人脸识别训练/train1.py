import cv2
import numpy as np

#加载「分类器」
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)       #开启本机摄像头
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('E:\桌面文件\python类资料\仿生鱼\opencv\picture\output1.avi', fourcc, 20.0, (640,480))

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize=(10, 10))
    #上面这步是输入比例因子、邻近数和人脸检测的最小尺寸的参数
    out.write(img)
    for (x,y,w,h) in faces:
        cv2.putText( img, "No." + str(len(faces))+"handsome", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_color = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        eyes =eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0,255,0), 2)
           

        cv2.imshow('img',img)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    
            

cap.release()
cv2.destroyAllWindows()
