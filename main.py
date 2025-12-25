import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
import math
from helper_funcs import truncate_float

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable) 

    AsteroidField.containers = (updatable)
    AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    score = 0
    timer_minutes = 0
    timer_seconds = 0

    #Game Loop
    while(True):
        log_state()
        score_font = pygame.font.Font("freesansbold.ttf", 40)
        score_text = score_font.render(f"Score -  {str(score)}", True, (255, 255, 0))
        timer_font = pygame.font.Font("freesansbold.ttf", 40)
        timer_text = timer_font.render(f"{str(timer_minutes)} mins : {str(timer_seconds)} secs", True, (255, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("GAME OVER")
                game_over_screen = pygame.image.load("gameover.png")
                screen.blit(game_over_screen, (0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    score += 1
                    shot.kill()
        screen.fill("black")
        screen.blit(score_text, (10,10))
        screen.blit(timer_text, (10,50))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        timer_seconds += dt
        timer_seconds = truncate_float(timer_seconds)
        if timer_seconds >= 60:
            timer_minutes += 1
            timer_seconds = 0

if __name__ == "__main__":
    main()
