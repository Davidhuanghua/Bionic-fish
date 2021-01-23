import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')  # 保存视频的编码
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 图像反转：1：水平翻转；0：垂直翻转 -1：水平垂直翻转
        frame = cv.flip(frame, 0)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
