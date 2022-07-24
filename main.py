from ast import IsNot
from msilib.schema import ControlCondition
import sys
from re import X
from numpy import size
import pygame
import time 
import random


'''
    TODO:

    change color of font while rendering
    check if both fonts are important
    create character (pixel art)

    make nice particles
'''



running = True
NAME = "2D Game"
VERSION = "0.0.1"
WIDTH = 800
HEIGHT = 600

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(NAME + " " + VERSION)

# Funcs/Classes ---------------------------------------------- #
def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()

class Font():
    def __init__(self, path):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert()
        font_img.set_colorkey((0, 0, 0))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def render(self, surf, text, loc, size):
        x_offset = 0
        for char in text:
            if char != ' ':
                current = self.characters[char]
                current = pygame.transform.scale(current, (current.get_width() * size, current.get_height() * size))
                surf.blit(current, (loc[0] + x_offset, loc[1]))
                x_offset += current.get_width() + self.spacing * size
            else:
                x_offset += self.space_width * size + self.spacing * size

# Init ------------------------------------------------------- #





my_font = Font('fonts\small_font.png')
my_big_font = Font('fonts\large_font.png')

start_time = time.time()

current_fps = 0
fps = 0

while running:


    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_d:
                pass

    current_fps += 1
    if time.time() - start_time >= 1 :
        start_time = time.time()
        fps = current_fps
        current_fps = 0

        
            
    
    # reset screen
    screen.fill((35, 39, 42))


    my_big_font.render(screen, f"Fps: {fps}", (5, 5), 2)
    my_font.render(screen, 'Test  1234 ABC XX', (100, 100), 2)
    
    
    # update display
    pygame.display.update()
        


    


