import pygame
from circleshape import CircleShape  # <- Player braucht CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE_SECONDS, LINE_WIDTH
from logger import log_state, log_event
import random


class Asteroid(CircleShape):  # <- Asteroid IST EINE Art von CircleShape
    def __init__(self, x, y, radius):  # <- Wenn jemand einen Asteroid erstellt, gibt er x, y und den Radius
        super().__init__(x, y, radius)  
        

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            circle_1 = Asteroid(self.position.x, self.position.y, new_r)
            circle_1.velocity = v1 * 1.2 
            circle_2 = Asteroid(self.position.x, self.position.y, new_r)
            circle_2.velocity = v2 * 1.2 

            
  