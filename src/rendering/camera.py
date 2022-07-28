from pygame import Surface


from utils.box import Box

class Camera():
    def __init__(self, x: float, y: float, width: int, height: int) -> bool:
        # these coordinates are kind of useless but they make it easier 
        self.x = x
        self.y = y
        # create box with screen width
        # this box is the screen or camera area
        self.box = Box(width, height)
        # offset the camera to the coordinates
        self.box.offset(x, y)

    def move(self, x: float, y: float):
        self.x += x
        self.y += y
        self.box.offset(self.x, self.y)
    def move_to(self, x: float, y: float):
        self.x = x
        self.y = y
        self.box.offset(self.x, self.y)
    '''
    This method defines if a game object should be rendered
    It returns true if some part of the object is in the camera area
    '''
    def should_render(self, object: Box)-> bool:
        if self.box.max_x < object.min_x or self.box.max_y < object.min_y:
            return False
        if self.box.min_x > object.max_x or self.box.min_y > object.max_y:
            return False
        return True