from pygame import Surface
import pygame
from utils.box import Box   

class WorldObject():
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.box = Box(x, y, width, height)

    def render(self, surface: Surface, offset_x: float, offset_y: float):
        offset_box = self.box
        offset_box.offset(offset_x, offset_y)
        pygame.draw.rect(surface, (255, 255, 255), (offset_box.min_x, offset_box.min_x, offset_box.get_width(), offset_box.get_height()))