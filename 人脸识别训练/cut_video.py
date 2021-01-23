# -*- coding:utf-8 -*- 

import cv2
import os
i=1
path='/'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def main():
    global path
    print('请把要处理的视频文件与该脚本放在放在同一目录!!\n')
    name = input('请输入视频名字（不用带后缀）：')
    print('\n正在处理视频...请稍等')
    filepath = os.getcwd()
    path = filepath+'\\'+name
    cap = cv2.VideoCapture(filepath+'\\'+name+'.MP4')
    mkdir(path)
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            catchface(frame)
        else:
            os.system('cls')
            print('视频中的人脸数据已全部采集！\n\n人脸数据在目录下'+name+'文件夹中')
            break
    dirList = os.listdir(path)
    mkcsv(dirList,path)
    
    
    cap.release()
    cv2.destroyAllWindows()
    i=input('\n输入任意字符退出程序...')
    os._exit(0)



def mkcsv(dirList,path):
    label = -1
    for name in dirList:
        #path = path + str(name)+'\\'
        print(path)
        cpath = str(path)[16:str(path).rfind('/'+'1')]
        
        label +=1
        f = open(path+'train.csv', 'a+') 
        fileList = os.listdir(path)
        for fileName in fileList:
            print(fileName)
            f.write(cpath + fileName + ';' + str(label) + '\n')
    
def catchface(frame):
    global i
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in faces:
        img = frame[y:y+h,x:x+w]
        cv2.imencode('.jpg', img)[1].tofile(path+'/'+str(i)+'.jpg')
        i+=1
    
def mkdir(path):  
    folder = os.path.exists(path)  
    if not folder:                 
        os.makedirs(path) 

main()
    
