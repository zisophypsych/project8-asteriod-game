import pygame 
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)  
    asteroid_field = AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        
        # player.draw(screen)
        # player.update(dt)

        for thing in drawable:
            thing.draw(screen)

        for thing in updatable:
            thing.update(dt)

        for thing in asteroids:
            if thing.check_collisions(player):
                print("Game Over!")
                sys.exit()
            

        pygame.display.flip()

        
        



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

