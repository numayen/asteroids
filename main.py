# IMPORT starts here #################################################
import pygame
from constants import *
from player import Player
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
    Player.containers = (updatable, drawable) #container for all players
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #in the middle of screen
    # INITIALIZE ends here
    ########################################################################


    # infinite game loop starts here
    ######################################################################
    while True:

        # check for user quitting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # calculate state according to player input
        #################################################################
        updatable.update(dt)
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