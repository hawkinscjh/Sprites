import pygame, sys, random

from pygame.constants import KEYDOWN

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        # Inheritance from Sprite class
        super().__init__()
        # Create empty surface image with given height and width
        self.image = pygame.image.load(picture_path)
        # Draw rectangle around surface
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('gunshot.wav')
    
    def shoot(self):
        self.gunshot.play()
        # When crosshair overlaps group, will remove target_group
        pygame.sprite.spritecollide(crosshair, target_group, True)

    # Update mouse pointer to crosshair image
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game screen
screen_width =  800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.png')
# Hide mouse pointer inside game. Will replace with crosshair
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair('crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

        pygame.display.flip()
        screen.blit(background, (0,0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        clock.tick(60)