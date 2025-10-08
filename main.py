import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroids_group, update_group, draw_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shots_group, update_group, draw_group)

    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    player = Player(player_start_x, player_start_y)
    asteroidField = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Physics
        update_group.update(dt)

        for asteroid in asteroids_group:
            if asteroid.has_collided(player):
                print("Game over!")
                return
            
            for shot in shots_group:
                if asteroid.has_collided(shot):
                    asteroid.split()
                    shot.kill()
            
        

        # Render
        screen.fill("black")

        for obj in draw_group:
            obj.draw(screen)    
    
        pygame.display.flip()
        dt = clock.tick(fps) / 1000


if __name__ == "__main__":
    main()
