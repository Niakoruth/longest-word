import string
import random
import requests

class Game:
    def __init__(self):
        self.grid = []
        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if word == '':
            return False
        grid_letters = list(self.grid)  # creating a copy of the grid object as a list
        for letter in word:
            if letter in grid_letters:
                grid_letters.remove(letter)
            else:
                return False
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        result = response.json()
        return result['found']
