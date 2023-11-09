from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion II."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        path = Path('high_score.txt')
        high_score = path.read_text()
        self.high_score = int(high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1