# IMPORT #################################################
import pygame
from circleshape import CircleShape
from constants import *
# IMPORT END #############################################

# class for Shots; same as asteroid but radius is static
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    # overrides method from parent; draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    # move the asteroid in a straight line with constant speed
    def update(self, dt):
        self.position += self.velocity * dt