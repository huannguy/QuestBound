import character
import pytest

@pytest.fixture
def setup():
    return character.Character()

def test_Character_object_Creation_Success(setup):
    assert setup._name == ""
    assert setup._position == 0
    assert setup._hp == character.STARTING_HP
    assert setup._skill_points == character.STARTING_SKILL_POINTS
    assert setup._coin_pouch == character.STARTING_COIN_AMOUNT

def test_is_at_destination(setup):
    setup._position == 0
    setup.is_at_destination() == False

    setup._position == character.DESTINATION
    setup.is_at_destination() == True



