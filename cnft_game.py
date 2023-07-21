```python
import random

class Game:
    def __init__(self, user):
        self.user = user
        self.points = 0
        self.xp = 0

    def play(self):
        self.points = random.randint(1, 100)
        self.xp = random.randint(1, 10)
        return self.points, self.xp

    def get_game_data(self):
        return {
            "user": self.user,
            "points": self.points,
            "xp": self.xp
        }
```