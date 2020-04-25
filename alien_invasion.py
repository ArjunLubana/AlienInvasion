import pygame
import sys
from settings import Settings
from ship import Ship
import os
from bullets import Bullet

class AlienInvasion:
    #Overall Class to manage game assets and behavior
    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        self.settings=Settings()
        self.bullets = pygame.sprite.Group()

        '''Sets the display size and caption'''
        self.screen = pygame.display.set_icon(pygame.image.load("images/icon.png"))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type ==pygame.KEYUP:
                    self._check_keyup_events(event)
                
    
    def _check_keydown_events(self,event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
         

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        '''Updates images on the screen and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


    def _fire_bullet(self):
        '''create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update Bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    os.chdir("/home/daphney/Python/AlienInvasion")
    ai = AlienInvasion()
    ai.run_game()