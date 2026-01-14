import random
import pygame
from logger import log_event
from circleshape import CircleShape
import constants


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, constants.LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        vec1 = self.position.rotate(angle)
        vec2 = self.position.rotate(-angle)

        radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position[0], self.position[1], radius)
        new1.velocity = vec1 * 1.2

        new2 = Asteroid(self.position[0], self.position[1], radius)
        new2.velocity = vec2 * 1.2
