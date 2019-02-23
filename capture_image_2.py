import picamera
import picamera.array
import time
import cv2
#from matplotlib import pyplot as plt
#import Tkinter 
#import Image, ImageTk
import sys

def capturePiCam():
    with picamera.PiCamera() as camera:
        cap=picamera.array.PiRGBArray(camera)
        camera.resolution = (320, 240)
        camera.start_preview()
        time.sleep(3)
        camera.capture(cap,format="bgr")
        global img
        img =cap.array

#- display on OpenCV window -
def displayAtOpenCV():
    cv2.namedWindow('imageWindow', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('imageWindow',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
