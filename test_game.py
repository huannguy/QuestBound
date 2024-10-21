import game
import pytest

@pytest.fixture
def setup():
    return game.Game()

def test_Game_object_Creation_Success(setup):
    assert setup._turn == 1