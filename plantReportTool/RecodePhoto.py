# -*- coding: utf-8 -*-
import cv2
import numpy
import os,time
from datetime import datetime
cap=cv2.VideoCapture(0)#ImageDevice選択 これしか見つからなかったけどww
#env=os.getenv("USERPROFILE")
env=os.path.abspath(os.path.dirname(__file__))#保存先の記載defaltでは ./plant_pictures に保存
env=os.path.join(env,"plant_pictures")

def ImageCaputureEveryHour():
    """
    this method is taka a picture every hour
    return save picture path
    defaultPath is 
    """
    now=int(time.strftime('%H'))
    while True:
        if int(time.strftime('%H'))-now==1 or int(time.strftime('%H'))-now==-23:
            path=takePicture()
            now=int(time.strftime('%H'))
            print(path)
        else:
            time.sleep(600)
def takePicture():
    timeNow = time.strftime('%Y%m%d%H')
    print("保存先は%sです。"%env)
    if not(os.path.exists(env)): 
        os.mkdir(env)
#        os.mkdirs(env)
    path = os.path.join(env,timeNow+".png")
    ret,frame=cap.read()
    if ret:
        if cv2.imwrite(path,frame):
            print("Success take and save a picture")
            print("path:"+path)
            return path
        else:
            print("Failed save picture")
    else:
        print("Failed take a picture")
#memo
#cv2.add()#写真を足し合わせる
#cv2.reduce()#写真を消し合わせるsample>>  cv2.reduce(src, dim, rtype[, dst[, dtype]]
def DeviceCount():
    """
    count videoCaptureDevice number
    argumet is nothing
    """
    cap=cv2.VideoCapture(a)
    if cap.isOpened():
        print ("open:"+str(a))
    else:
        print("Fail:"+str(a))
if __name__ == '__main__' :
    ImageCaputureEveryHour()