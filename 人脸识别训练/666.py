import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)      


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640,480))

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(5, 5))

    out.write(img)
    for (x,y,w,h) in faces:
        cv2.putText(img, "No." + str(len(faces))+"handsome", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        cv2.putText(img,'unknow',(x,y),cv2.FONT_HERSHEY_SIMPLEX,2, (0,0,255),2)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_color = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        eyes =eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),(0,255,0), 2)
     
        cv2.resizeWindow('img', 600, 450)
        cv2.imshow('img',img)       
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
    
            

cap.release()
out.release()
cv2.destroyAllWindows()
