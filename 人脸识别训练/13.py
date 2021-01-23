import face_recognition
import cv2
import time


def see():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 导入人脸
    m1_image = face_recognition.load_image_file("./david.jpg")
    m1_face_encoding = face_recognition.face_encodings(m1_image)[0]

    face_locations = []

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
                match = face_recognition.compare_faces(faces_to_compare, face_encoding, tolerance=0.35)
                name = "Unknown"
                print(match)

                if match[0]:
                    name = "administrator"  # 此为管理员

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
        cv2.resizeWindow('video', 600, 500)
        cv2.imshow('video', frame)

        # 按q退出程序。
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 清空数据，关闭所有窗口；
    cap.release()
    cv2.destroyAllWindows()
    print('video close successfully ')


if __name__ == '__main__':
    see()
