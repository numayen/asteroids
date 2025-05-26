# IMPORT #################################################
import pygame
import random
from circleshape import CircleShape
from constants import *
# IMPORT END #############################################

# class for Asteroids
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    # overrides method from parent; draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    # move the asteroid in a straight line with constant speed
    def update(self, dt):
        self.position += self.velocity * dt

    # behavior on hit by shot
    def split(self):
        self.kill() #delete current asteroid
        if self.radius < ASTEROID_MIN_RADIUS: #no new asteroids under min radius
            self.kill()
            return
        split_angle = random.uniform(SPLIT_ANGLE_MIN, SPLIT_ANGLE_MAX) #random split angle
        new_velocity_one = self.velocity.rotate(split_angle) #new velocity rotated by random angle
        new_velocity_two = self.velocity.rotate(-split_angle) #other velocity in other direction
        new_radius = self.radius - ASTEROID_MIN_RADIUS #make new asteroids smaller
        
        #create new asteroids
        new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_one.velocity = new_velocity_one * SPLIT_UPSPEED
        new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_two.velocity = new_velocity_two * SPLIT_UPSPEED
        self.kill()