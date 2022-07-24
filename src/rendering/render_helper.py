import time 

class RenderHelper():
    def __init__(self) -> None:
        # public varibles
        self.fps = 0
        self.delta_time = 0
        # private variables
        self._current_fps = 0
        self._start_time = 0
        self._last_time = 0
    def update(self):

        self.delta_time = time.time() - self._last_time
        self.delta_time *= self.fps
        self._last_time = time.time()

        self._current_fps += 1
        if time.time() - self._start_time >= 1:
            self._start_time = time.time()
            self.fps = self._current_fps
            self._current_fps = 0
