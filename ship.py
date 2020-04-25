import pygame

class Ship:
    #A Class to manage ship

    def __init__(self,ai_game):
        #Initialize the ship and set its starting position
        self.screen=ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #Load ship image and get its Rect
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()

        #Start each ship at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Ship Movement Flags
        self.moving_right=False
        self.moving_left=False
    def blitme(self):
        #Draw the ship at it's current position
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        '''Update the ship's position based on the movement flags'''
        #Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update the rect object from self.x
        self.rect.x = self.x
