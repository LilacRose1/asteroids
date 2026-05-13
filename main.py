import pygame
from constants import *
from logger import log_state

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
        pygame.display.flip() 
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
