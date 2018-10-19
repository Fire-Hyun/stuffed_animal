# -*- coding: utf-8 -*-

import pygame
import RPi.GPIO as GPIO
from time import sleep

Button = 18

GPIO.setmode (GPIO.BCM)  # GPIO 모드 세팅

GPIO.setup(Button, GPIO.IN)  # 버튼 입력으로 설정

pygame.init()
pygame.mixer.init()

try:
        while True:
                if GPIO.input(Button)==0:
                    pygame.mixer.music.load("book.wav")
                    pygame.mixer.music.play()

except KeyboardInterrupt:
        GPIO.cleanup()
