from picamera import PiCamera
from time import sleep
import time
import datetime
import os

camera = picamera.PICamera()
camera.start_preview()
#saveFileName = datetime.datetime.now().strftime('%y%m%d-%H%M%S%f')+'.h264'
camera.start_recording('/home/pi/2018_10_29.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()
os.system("MP4Box -add 2018_10_29.h264 2018_10_29.mp4")

