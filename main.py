import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        player.draw(screen)

        pygame.display.flip() 
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
