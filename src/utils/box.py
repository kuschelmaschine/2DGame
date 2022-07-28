class Box():
    def __init__(self, min_x: float, min_y: float, max_x: float, max_y: float) -> None:
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
    def __init__(self, width: float, height: float) -> None:
        self.min_x = 0
        self.min_y = 0
        self.max_x = width
        self.max_y = height

    def get_width(self):
        return self.max_x - self.min_x
    def get_height(self):
        return self.max_y - self.min_y
    def offset(self, x: float, y: float):
        self.min_x += x
        self.max_x += x
        self.min_y += y
        self.max_y += y
    