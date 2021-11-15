#Before Installing , Open CMD (make sure you have pip installed) and type "pip install pygame"

import pygame, sys, random
from pygame.locals import *
from pygame import mixer 

WIDTH = 800 #1920
HEIGHT = 800 #1080
screen_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # adding ~pygame.RESIZABLE~ at the end of 1st bracket makes it Resizable
clock = pygame.time.Clock()
screen_rect = screen.get_rect() 

class Background:
    def solid_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        screen.fill((red, green, blue))
    def Image(self, image):
        self.image = pygame.image.load(image)
        self.image_size = [self.image.get_width(), self.image.get_height()]
        if (self.image_size[0] == WIDTH) and (self.image_size[1] == HEIGHT):
            screen.blit(image, [0, 0])
        elif (self.image_size[0] >= WIDTH/2 and self.image_size[0] <= WIDTH) or (self.image_size[1] >= HEIGHT/2 and self.image_size[1] <= HEIGHT):
            self.new_image = pygame.transform.scale(self.image, screen_size)
            screen.blit(self.new_image, [0, 0])
        elif (self.image_size[0]>= WIDTH*11/110 and self.image_size[0] <= WIDTH*3/2) or (self.image_size[1]>= HEIGHT*11/110 and self.image_size[1] <= HEIGHT*3/2):
            self.new_image = pygame.transform.scale(self.image, screen_size)
            screen.blit(self.new_image, [0, 0])
        else:
            print("Invalid Image Size!") 

class Entity:
    def __init__(self, x, y, vel_x, vel_y, sprite):
        self.x = x
        self.y = y 
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.sprite = sprite

    def render(self):
        self.bad_img = pygame.image.load(self.sprite)
        self.image_height, self.image_width = 50, 50
        self.sprite_size = (self.image_height, self.image_width)

        self.img = pygame.transform.scale(self.bad_img, self.sprite_size)
        screen.blit(self.img, [self.x, self.y])    

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y


player = Entity(100, 100, 3, 3, "Image Location")    # x, y, vel_x, vel_y, sprite
background = Background()
while True:
    background.Image("Image Location")
    keys = pygame.key.get_pressed()
    for ev in pygame.event.get():
        if ev.type == QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit() 

    player.render()

    pygame.display.update()
    clock.tick(60)

"""For now , The code is very simple and Tiny
I'll be adding other features in Future
