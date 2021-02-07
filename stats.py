class GameStats:

    def __init__(self, settings):
        self.score = 0
        self.settings = settings
        self.reset_stats()

        self.game_active = False

        self.level1 = False
        self.level2 = False
        self.level3 = False
        self.level4 = False

    def reset_stats(self):
        pass
