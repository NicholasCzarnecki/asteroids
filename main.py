import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    score = 0
    dt = 0  # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for object in updatable:
            object.update(dt)
        for object in asteroids:
            for shot in shots:
                if object.collision_check(shot):
                    object.split()
                    shot.kill()
                    score += 1
            if object.collision_check(player):
                print("Game over!")
                sys.exit(0)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit frame rate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
