import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    

    def __init__(self, x, y):
        
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__shot_timer = 0
    
    
    # in the player class
    def triangle(self):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def rotate(self, dt):

        self.rotation += PLAYER_TURN_SPEED * dt
    
    
    def move(self, dt):

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        if self.__shot_timer > 0:
            return 
        
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot.velocity *= PLAYER_SHOOT_SPEED
        self.__shot_timer = PLAYER_SHOOT_COOLDOWN


    def draw(self, screen):

        pygame.draw.polygon(screen, "white", self.triangle(), 2)

   
    def update(self, dt):

        self.__shot_timer -= dt

        keys = pygame.key.get_pressed()
        
        # Left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        # Right
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # Forwards
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

