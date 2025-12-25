from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            log_event("asteroid_destroyed")
            return
        else:
            log_event("asteroid_split")
            random_angle_1 = random.uniform(20, 50)
            new_vector_1 = self.velocity.rotate(random_angle_1)
            random_angle_2 = random.uniform(-50, -20)
            new_vector_2 = self.velocity.rotate(random_angle_2)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = new_vector_1 * 1.2
            new_asteroid_2.velocity = new_vector_2 * 1.2