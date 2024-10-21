import hierarchy
from random import randint
import numpy as np
import unittest
from unittest.mock import patch
import pytest

###################### RUN TEST BY typing pytest ######################

# TESTING THE ACTION CLASS'S METHODS

#Tests the default constructor for the Action class.
def test_Action_Object_Creation_Success():
    object = hierarchy.Action()
    assert object._proficiency_lvl == 1

def test_is_skills_maxed(): 
    object = hierarchy.Action()

    #Tests if the is_skill_maxed() function returns True if the action's
    #proficiency level is equal to the skill cap, which is 3. 
    object._proficiency_lvl = hierarchy.SKILL_CAP    #SKILL_CAP = 3
    assert object.is_skill_maxed() == True

    #Tests if the is_skill_maxed() function returns False if the action's
    #proficiency level is less the skill cap, which is 3. 
    object._proficiency_lvl = 2
    assert object.is_skill_maxed() == False

def test_invest_skill_points():
    object = hierarchy.Action()
    skill_points = 10

    #Tests if the invest_skill_points() function returns 1 if the action's
    #proficiency level is equal to the skill cap, which is 3.
    object._proficiency_lvl = hierarchy.SKILL_CAP   #SKILL_CAP = 3
    assert object.invest_skill_points(skill_points) == 0

    #Tests if the invest_skill_points() function returns 1 if the action's
    #proficiency level is 1.
    object._proficiency_lvl = 1
    assert object.invest_skill_points(skill_points) == 2

    #Tests if the invest_skill_points() function returns 1 if the action's
    #proficiency level is 2.
    object._proficiency_lvl = 2
    assert object.invest_skill_points(skill_points) == 2 

    #Tests if the invest_skill_points() function raises a ValueError exception 
    #if a negative number was passed into the function call.
    with pytest.raises(ValueError):
        object.invest_skill_points(-1) 
    
def test_reset_proficiency_lvl():
    object = hierarchy.Action()

    #Tests if the reset_proficiency_lvl() function returns 0 if the action's
    #proficiency level is 1.
    object._proficiency_lvl = 1
    assert object.reset_proficiency_lvl() == 0

    #Tests if the reset_proficiency_lvl() function returns the number of skill
    #points invested in the action if the action's proficiency level is not one.
    object._proficiency_lvl = 2
    temp = object._proficiency_lvl
    assert object.reset_proficiency_lvl() == temp * hierarchy.SKILL_POINT_COST

    #Tests if the action's proficiency level is zero after the the function
    #was executed.
    assert object._proficiency_lvl == 1


# TESTING THE SWORDFIGHTING CLASS'S METHODS

#Tests the default constructor for the Action class.
def test_SwordFighting_Object_Creation_Success():
    object = hierarchy.SwordFighting()
    assert object._sword_lvl == 1

def test_attack():
    object = hierarchy.SwordFighting()

    assert object.attack() == object._sword_lvl * object._proficiency_lvl * hierarchy.DAMAGE_OUTPUT

    #Tests if the attack() function returns the correct damage output when the
    #proficiency level is set to 1 and the sword level is set to 2.
    object._proficiency_lvl = 2
    object.sword_lvl = 2
    assert object.attack() == object._sword_lvl * object._proficiency_lvl * hierarchy.DAMAGE_OUTPUT

def test_dodge():
    object = hierarchy.SwordFighting()

    result = object.dodge()
    assert result == 0 or result == 1

def test_upgrade_sword():
    object = hierarchy.SwordFighting()
    coin_pouch = 30

    #Tests if the upgrade_sword() function raises a ValueError exception if
    #a negative number was passed into the function call.
    with pytest.raises(ValueError):
        object.upgrade_sword(-1) 
    
    #Test if the upgrade_sword_lvl() function is returning 0 if the sword level 
    #cannot be upgraded further.
    object._sword_lvl = 3
    assert object.upgrade_sword(coin_pouch) == 0

    #Tests if the sword level is still the same level if the upgrade_sword()
    #returns 0.
    assert object._sword_lvl == 3

    #Test if the upgrade+sword_lvl() function is returning 1 if the player
    #does not have coins to afford the purchase.
    object._sword_lvl = 2
    assert object.upgrade_sword(0) == 1
    assert object._sword_lvl == 2

    #Test if the upgrade_sword_lvl() function is returning 1 if the sword level 
    #was upgraded.
    object._sword_lvl = 1
    assert object.upgrade_sword(coin_pouch) == 2
    assert object._sword_lvl == 2 
    
# TESTING THE ASSISTING CLASS'S METHODS

#Tests the default constructor for the Assisting class.
def test_Assisting_Object_Creation_Success():
    object = hierarchy.Assisting()

    assert object._assistance_count == 0

@patch('builtins.input', return_value='n')
def test_assist_with_no_input(mock_input):
    object = hierarchy.Assisting()

    #Test if the assist() function returns 0
    #if the user enter 'n' for no.
    result = object.assist()
    assert result >= 0

@patch('builtins.input', return_value='y')
def test_assist_with_yes_input(mock_input):
    object = hierarchy.Assisting()

    #Test if the assist() function returns 15
    #or greater if the user enter 'y' for yes.
    result = object.assist()
    assert result >= 15

def test_generate_reward():
    object = hierarchy.Assisting()

    #Test if the generate_reward() function is returning 
    #at least 15, representing the amount of
    #coins the player will receive for providing
    #assistance.
    assert object.generate_reward() >= 15

def test_generate_scenario():
    object = hierarchy.Assisting()

    #Test if the generate_request() function is returning a integer
    #between 1-5, representing the scenario that
    #was generated.
    result = object.generate_request() 
    assert result >= 1 and result <= 5

# TESTING THE HEALING CLASS'S METHODS

#Tests the default constructor for the Healing class.
def test_Healing_Object_Creation_Success():
    object = hierarchy.Healing()

    #Tests if the _healing_items attribute of the object object is equal to the
    #specified list.
    assert object._healing_items == ["Healing Salve", "Healing Poultice", "Healing Potion"]

    #Tests if the _inventory attribute of the object object is equal to a 
    #specific array (or list).
    assert np.array_equal(object._inventory, ([0, 0, 0]))


@patch('builtins.input', return_value = 1)
def test_apply_treatment_healing_salve(mock_input):
    object = hierarchy.Healing()

    #Tests if the apply_treatment() function returns 0 if the
    #player has zero healing items.
    assert object.apply_treatment() == 0

    object._inventory[0] = 1

    #Tests if the apply_treatment() function returns a restore
    #amount of 5 if the player's has at least one healing salve
    #in their healing items inventory.
    assert object.apply_treatment() == hierarchy.SALVE_RESTORE

@patch('builtins.input', return_value = 2)
def test_apply_treatment_healing_poultice(mock_input):
    object = hierarchy.Healing()

    #Tests if the apply_treatment() function returns 0 if the
    #player has zero healing items.
    assert object.apply_treatment() == 0

    object._inventory[1] = 1

    #Tests if the apply_treatment() function returns a restore
    #amount of 10 if the player's has at least one healing poultice
    #in their healing items inventory.
    assert object.apply_treatment() == hierarchy.POULTICE_RESTORE

@patch('builtins.input', return_value = 3)
def test_apply_treatment_healing_potion(mock_input):
    object = hierarchy.Healing()

    #Tests if the apply_treatment() function returns 0 if the
    #player has zero healing items.
    assert object.apply_treatment() == 0

    object._inventory[2] = 1

    #Tests if the apply_treatment() function returns a restore
    #amount of 5 if the player's has at least one healing potion
    #in their healing items inventory.
    assert object.apply_treatment() == hierarchy.POTION_RESTORE


@patch('builtins.input', side_effect = [1, 2])
def test_purchase_healing_items_healing_salve(mock_input):
    object = hierarchy.Healing()
    coins = 20

    #Calculates the remaining coins after purchasing two healing
    #salves, which cost 5 coins each.
    remaining_coins = coins - 2 * hierarchy.SALVE_PRICE

    #Tests if the purchase_healing_items() function raises a ValueError 
    #exception if a negative number was passed into the function call.
    try:
        object.purchase_healing_items(-1)
    
    except ValueError:
        print("\ncoin_pouch must be a nonnegative number.")

    #Test if the return value of purchase_healing_items() is
    #equal to remaining_coins.
    assert object.purchase_healing_items(coins) == remaining_coins
    assert object._inventory[0] == 2

@patch('builtins.input', side_effect = [2, 2])
def test_purchase_healing_items_healing_poultice(mock_input):
    object = hierarchy.Healing()
    coins = 40

    #Calculates the remaining coins after purchasing two healing
    #poultices, which cost 10 coins each.
    remaining_coins = coins - 2 * hierarchy.POULTICE_PRICE

    #Tests if the purchase_healing_items() function raises a ValueError 
    #exception if a negative number was passed into the function call.
    try:
        object.purchase_healing_items(-1)
    
    except ValueError:
        print("\ncoin_pouch must be a nonnegative number.")

    #Test if the purchase_healing_items() returns a value that is 
    assert object.purchase_healing_items(coins) == remaining_coins

    #Test if player's now have two healing poultices in their
    #healing items inventory.
    assert object._inventory[1] == 2

@patch('builtins.input', side_effect = [3, 2])
def test_purchase_healing_items_healing_potion(mock_input):
    object = hierarchy.Healing()
    coins = 60

    #Calculates the remaining coins after purchasing one healing
    #potion, which cost 30 coins.
    remaining_coins = coins - 2 * hierarchy.POTION_PRICE

    #Tests if the purchase_healing_items() function raises a ValueError 
    #exception if a negative number was passed into the function call.
    try:
        object.purchase_healing_items(-1)
    
    except ValueError:
        print("\ncoin_pouch must be a nonnegative number.")

    #Test if the purchase_healing_items() returns a value that is 
    assert object.purchase_healing_items(coins) == remaining_coins

    #Test if player's now have two healing potions in their
    #healing items inventory.
    assert object._inventory[2] == 2


@patch('builtins.input', side_effect = [1, 2])
def test_sell_healing_items_healing_salve(mock_input):
    object = hierarchy.Healing()

    #Calculates the number of coins selling two healing salves
    #will yield.
    profit = 2 * hierarchy.SALVE_PRICE

    object._inventory[0] = 5

    #Test if the return value of the sell_healing_items() 
    #function is equal to profit.
    assert object.sell_healing_items() == profit
    assert object._inventory[0] == 3

@patch('builtins.input', side_effect = [2, 2])
def test_sell_healing_items_healing_poultice(mock_input):
    object = hierarchy.Healing()

    #Calculates the number of coins selling two healing poultices
    #will yield.
    profit = 2 * hierarchy.POULTICE_PRICE

    object._inventory[1] = 5

    #Test if the return value of the sell_healing_items() 
    #function is equal to profit.
    assert object.sell_healing_items() == profit
    assert object._inventory[1] == 3

@patch('builtins.input', side_effect = [3, 2])
def test_sell_healing_items_healing_potion(mock_input):
    object = hierarchy.Healing()

    #Calculates the number of coins selling two healing potions
    #will yield.
    profit = 2 * hierarchy.POTION_PRICE

    object._inventory[2] = 5

    #Test if the return value of the sell_healing_items() 
    #function is equal to profit.
    assert object.sell_healing_items() == profit
    assert object._inventory[2] == 3



