from platform import win32_edition
import cv2
import os
import numpy as np

# load = cv2.imread('sakurei1.jpeg',0) #第２引数 -1=無変換 0=グレー 1=カラー 2=任意の震度 3=任意のカラー
cap_file = cv2.VideoCapture('video.mp4')

frame_count = int(cap_file.get(cv2.CAP_PROP_FRAME_COUNT))
print('フレーム',frame_count)

previous_frame = []

for i in range(frame_count):
    ch,frame=cap_file.read()
    if ch:
        frame = cv2.resize(frame,(1080,1920))



        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        canny = cv2.Canny(gray,5,50)
        
        height = canny.shape[0]
        width = canny.shape[1]
        center = (int(width/2),int(height/2))

        angle = 180.0
        scale = 1.0
        trans = cv2.getRotationMatrix2D(center,angle,scale)
        image2 = cv2.warpAffine(canny,trans,(width,height))
        
        previous_frame.append(image2)

        cv2.imshow('movie',image2)
    k= cv2.waitKey(1)
    if k == 27:
        break

f = open('edited_movie.txt','w')
if f != None:
    f.write(str(previous_frame))
else:
    f.close()




