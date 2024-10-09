import pygame #pip install pygame
pygame.init()
pygame.mixer.music.load("arquivo.mp3")
pygame.mixer.music.play()
pygame.event.wait()