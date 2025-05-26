# IMPORT #################################################
import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *
# IMPORT END #############################################

# class for players
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    # method given by boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # method overrides parent; draw object to screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # rotate the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # move the player, given by boot.dev
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # method overrides parent; update rotation according to player inputs 
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt #update cooldown
        
        # if a got pressed rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # if d got pressed rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # if w got pressed move forward
        if keys[pygame.K_w]:
            self.move(dt)
        
        # if s got pressed move backward
        if keys[pygame.K_s]:
            self.move(-dt)

        # if spacebar got pressed and countdown <= 0 pressed shoot
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot()
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    # shoot a shot at player position in player direction
    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED