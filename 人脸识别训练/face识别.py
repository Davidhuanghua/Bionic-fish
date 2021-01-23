import face_recognition
import cv2

#打开摄像头
video_capture = cv2.VideoCapture(0)

#传入人脸数据，让仿生鱼知道管理员
ad_img = face_recognition.load_image_file("img1.jpg")
ad_face_encoding = face_recognition.face_encodings(ad_img)[0]
#创建列表存放脸部特征数据
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    #读入视频数据
    ret, frame = video_capture.read()
    #创建小窗口，用来显示脸
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([obama_face_encoding], face_encoding)

            if match[0]:
                name = "Barack"
            else:
                name = "unknown"

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),  2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
