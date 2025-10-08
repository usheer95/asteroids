import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position.x, self.position.y
        asteroid_one = Asteroid(x, y, radius)
        asteroid_two = Asteroid(x, y, radius)

        angle = random.uniform(20, 50)
        asteroid_one.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_two.velocity = self.velocity.rotate(-angle) * 1.2

        
        
        