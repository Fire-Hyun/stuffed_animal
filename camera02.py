import picamera
import time
import datetime
import os

camera = picamera.PICamera()
camera.start_preview()
saveFileName = datetime.datetime.now().strftime('%y%m%d-%H%M%S%f')+'.h264'
camera.start_recording('/home/pi/saveFileName')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()
os.system("MP4Box -add saveFileName.h264 saveFileName.mp4")

