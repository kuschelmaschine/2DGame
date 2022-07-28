from pygame import Surface
from rendering.camera import Camera


class World():

    def __init__(self, surface: Surface) -> None:
        self.game_objects: list = []
        self.cam = Camera(0, 0, surface.get_width(), surface.get_height())
        

    def update(self, delta_time) -> bool:
        return True

    def render(self) -> bool:
        return True