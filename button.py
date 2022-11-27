import pygame
class Button:
    def __init__(self):
        self.price = 3
        self.level = 1   
    sprite = pygame.image.load('data/gfx/button.png')
    typeIndicatorSprite = pygame.image.load('data/gfx/null_indicator.png')

    def draw(self, DISPLAY, buttons, font_small, font_20):
        DISPLAY.blit(self.sprite, (220 + (buttons.index(self)*125), 393))
        priceDisplay = font_small.render(str(self.price), True, (0,0,0))
        DISPLAY.blit(priceDisplay, (262 + (buttons.index(self)*125), 408))
        levelDisplay = font_20.render('Lvl. ' + str(self.level), True, (200,200,200))
        DISPLAY.blit(levelDisplay, (234 + (buttons.index(self)*125), 441))
        DISPLAY.blit(self.typeIndicatorSprite, (202 + (buttons.index(self)*125), 377))