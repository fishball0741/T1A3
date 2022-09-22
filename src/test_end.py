from battle import end_game
import pytest

inputs = ['yes', 'no']

class TestEnd:
    def test_end_game(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        assert end_game(yes) is main.main()
        assert end_game(no) is exit()


