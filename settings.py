class Settings:
    """A class to store all settings for Alien Invaton II. """

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen steeings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Alien settings.
        self.alien_speed = 1.5
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 15

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.8
        self.bullet_speed = 2.8
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50 

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)