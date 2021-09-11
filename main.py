import pygame, sys, random

from pygame.constants import KEYDOWN

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, score):
        # Inheritance from Sprite class
        super().__init__()
        # Create empty surface image with given height and width
        self.image = pygame.image.load(picture_path)
        # Draw rectangle around surface
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound('gunshot.wav')
        self.score = 0
    
    def shoot(self):
        self.gunshot.play()
        # When crosshair overlaps group, will remove target_group
        if pygame.sprite.spritecollide(crosshair, target_group, True):
        
            self.score += 1
            print(self.score)

    # Update mouse pointer to crosshair image
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

        # Drawing
        screen.blit(background, (0,0))
        screen.blit(ready_text, (screen_width/2 - 118, screen_height/2 - 40))
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
        
        if crosshair.score >= 5:
            self.state = 'game_over'

        # Drawing
        screen.blit(background, (0,0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        # Drawing
        screen.blit(background, (0,0))
        screen.blit(over_text, (screen_width/2 - 118, screen_height/2 - 40))
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'game_over':
            self.game_over()

# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Game screen
screen_width =  800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('background.png')
# Hide mouse pointer inside game. Will replace with crosshair
pygame.mouse.set_visible(False)
# Font and text for intro
center_font = pygame.font.Font('freesansbold.ttf', 64)
ready_text = center_font.render("READY", True, (255, 255, 255))
over_text = center_font.render("GAME OVER", True, (255, 255, 255))

# Crosshair
crosshair = Crosshair('crosshair.png', 0)
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('target.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

# Main game loop
while True:
        game_state.state_manager()
        clock.tick(60)