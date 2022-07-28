import time

from pygame import Surface

class Particle():
    def __init__(self, x: float, y: float, vel_x: float, vel_y: float) -> None:
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.init_time = time.time()
    def update(self, delta_time):
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time 


class ParticleSystem():

    def __init__(self, delay: int, remove_of_screen: bool):
        self.particles: list = []
        self.particle_params = 4
        self.remove_of_screen = remove_of_screen
        self.delay = delay

    def add(self, particle: Particle):
        self.particles.append(particle)
    def update(self, surface: Surface, delta_time):
        for i in range(len(self.particles)-1, -1, -1):
            if (time.time() - self.particles[i].init_time >= self.delay) or not self.should_render_particle(surface, i):
                self.particles.pop(i)
                
            else:
                self.particles[i].update(delta_time)
    def should_render_particle(self, surface: Surface, index: int) -> bool:
        if self.particles[index].x < 0 or self.particles[index].x > surface.get_width():
            return False
        if self.particles[index].y < 0 or self.particles[index].y > surface.get_height():
            return False
        return True