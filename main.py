import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Courier New', 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (updateables, drawables, asteroids)
    AsteroidField.containers = (updateables)
    Shot.containers = (updateables, drawables, shots)

    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill("black")

        for updateable in updateables:
            updateable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

            if asteroid.is_colliding(player):
                text = font.render('Game over!', True, 'white')
                text_width, text_height = text.get_width(), text.get_height()
                screen.blit(text, (SCREEN_WIDTH / 2 - text_width / 2, SCREEN_HEIGHT / 2 - text_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(fps) / 1000

if __name__ == "__main__":
    main()
