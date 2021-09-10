import pygame, sys

from pygame.constants import KEYDOWN

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        # Inheritance from Sprite class
        super().__init__()
        # Create empty surface image with given height and width
        self.image = pygame.Surface([width, height])
        # Fill empty surface with color
        self.image.fill(color)
        # Draw rectangle around surface
        self.rect = self.image.get_rect()
        # Position rectangle at X and Y coordinate
        self.rect.center = [pos_x, pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width =  800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Width and Height = 50 pixels, X and Y positions = 100, color = white (255, 255, 255)
crosshair = Crosshair(50,50,100,100,(255,255,255))

# Add group of crosshairs
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)



# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        crosshair_group.draw(screen)
        clock.tick(60)