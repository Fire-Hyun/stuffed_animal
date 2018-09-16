import pygame
import time

pygame.mixer.init()
Sound = pygame.mixer.Sound("test.wav")
while True:
Sound.play()
time.sleep(2.0)