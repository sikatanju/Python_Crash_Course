class Settings: # * A class to store all settings for Alien Invasion.
    def __init__(self):
        # * Screen settings
        self.screen_width = 1600
        self.scree_height = 900
        self.bg_color = (230, 230, 230)
        
        # * Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # * Bullet Settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10   

        # * Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 450
        self.fleet_direction = 1
