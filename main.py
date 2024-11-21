import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawble_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawble_group)
    Asteroid.containers = (updatable_group, drawble_group, asteroid_group)
    AsteroidField.containers = (updatable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatable_group:
            updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.is_colliding(player):
                print("Game over!")
                exit()

        screen.fill("black")

        for drawble in drawble_group:
            drawble.draw(screen)

        pygame.display.flip()

        #limit FPS to 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
