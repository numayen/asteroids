# IMPORT starts here #################################################
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# IMPORT ends here #############################################

def main():
    # INITIALIZE starts here
    #####################################################################
    pygame.init() #pygame functions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #screen to draw on
    clock = pygame.time.Clock() #clock object
    dt = 0 # delta time from clock
    updatable = pygame.sprite.Group() #group of updatable objects
    drawable = pygame.sprite.Group() #group of drawable objects
    asteroids = pygame.sprite.Group() #group of all asteroids
    Player.containers = (updatable, drawable) #player is always updatable and drawable
    Asteroid.containers = (asteroids, updatable, drawable) #asteroids are always updatable and drawable
    AsteroidField.containers = (updatable) #asteroid field is not drawable and no asteroid object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #in the middle of screen
    asteroid_field = AsteroidField() #the asteroid field
    # INITIALIZE ends here
    ########################################################################


    # infinite game loop starts here
    ######################################################################
    while True:

        # check for user quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # calculate state
        #################################################################
        updatable.update(dt) #move according to player input
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
        # state calculation ends here
        ##################################################################


        # start drawing on screen
        ##################################################################
        screen.fill("black") #black canvas
        for thing in drawable: #draw all drawables
            thing.draw(screen)
        # finish drawing on screen
        ##################################################################
        
        
        # update display
        pygame.display.flip()

        # limit frame rate, dt time passed in s
        dt = clock.tick(FRAMERATE_LIMIT) / 1000
    # infinite game loop ends here
    ######################################################################








# convention for calling main
if __name__ == "__main__":
    main()