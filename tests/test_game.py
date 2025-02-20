from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        new = Game()

        # exercise
        grid = new.grid

        # verify
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_is_invalid(self):
        new = Game()
        test = []
        assert new.is_valid(test) is False

    def test_is_valid(self):
        new = Game()
        test_grid = "POIUYTREW"
        test_word = "POETRY"

        new.grid = list(test_grid) # calling class object

        #test scenarios
        assert new.is_valid(test_word) is True
        assert new.grid == list(test_grid) # making sure the grid is unchanged

    def test_is_invalid(self):
        new = Game()
        test_grid = "POIUYTREW"
        test_word = "EUREKA"

        new.grid = list(test_grid) # calling class object

        #test scenarios
        assert new.is_valid(test_word) is False
        assert new.grid == list(test_grid) # making sure the grid is unchanged
