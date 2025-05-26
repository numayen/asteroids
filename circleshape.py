import pygame

# class mostly given by boot.dev; added collision method later
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # check for collision with another circle, returns true in case of collision
    def collision(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        return distance < (self.radius + other_circle.radius)