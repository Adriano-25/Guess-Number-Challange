import random
import time

# Dictionary to store player scores (name: score)
leaderboard = {}

# Difficulty levels with their corresponding range and time limit
difficulty_levels = {
    "easy": {"range": (1, 10), "time_limit": 15},
    "medium": {"range": (1, 20), "time_limit": 10},
    "hard": {"range": (1, 50), "time_limit": 7}
}
print(difficulty_levels)