from typing import Any
import pygame


class CircleShape(pygame.sprite.Sprite):
    # Base class for game objects
    containers: Any
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: int

    def __init__(self, x: float, y: float, radius: int):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        # must override
        pass

    def update(self, dt: float):
        # must override
        pass

    def collides_with(self, other):
        dist = self.position.distance_to(other.position)
        return dist <= self.radius + other.radius
