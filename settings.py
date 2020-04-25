class Settings:
    #A Class to store all settings for Alien Invasion

    def __init__(self):
        #Initialize the game settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,230,230)
        self.ship_speed = 3.5
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3