#Thomas Hübscher / 24.02.2021
#self driving car project inspired by https://www.youtube.com/watch?v=Cy155O5R1Oo&ab_channel=NeuralNine

import math
import random
import sys
import os

import neat
import pygame


#create a pygame window

background_color = (255,255,255)
(width, height) = (1250,650)

screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption("Self Driving Car")
screen.fill(background_color)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




class Car:
    pass