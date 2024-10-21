# ******************************************************************************
# Author:      Huan Nguyen
# Date:        06/1/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   hierarchy.py
# Purpose:     This file contains the interfaces for the Action, SwordFighting,
#              Assisting, and Healing classes.
# ******************************************************************************
from random import randint
from numpy import array
import os
import time
import valid as v

#Constant to set the highest level of proficiency a character can attain in a
#skill.
SKILL_CAP = 3   

#Constant to define the number of skill points required for a character to
#increase their proficiency in a skill by one level.
SKILL_POINT_COST = 10

#Constant to set the highest level a sword can be upgraded to.
SWORD_LVL_MAX = 3   

SWORD_UPGRADE_COST = 30

#Constant to set the player's base damage output.
DAMAGE_OUTPUT = 25

#Constants to set the prices of healing items.
SALVE_PRICE = 5
POULTICE_PRICE = 10
POTION_PRICE = 15

#Constants to set the amount of health points each healing item restores.
SALVE_RESTORE = 10
POULTICE_RESTORE = 20
POTION_RESTORE = 30

#Interface for the Action class, which will serve as the super class of the hierarchy.
class Action:
    
    #Default constructor
    def __init__(self) -> None:
        self._proficiency_lvl = 1

    # **************************************************************************
    # Function to check if the current action's proficiency level is maxed.
    #
    # none
    #
    # The function returns false if the action's proficiency level is not
    # maxed. Otherwise, the function returns true if it is.
    # **************************************************************************
    def is_skill_maxed(self) -> bool:
        return self._proficiency_lvl == SKILL_CAP
 
    # **************************************************************************
    # Function to increase the current action's proficiency level.
    #
    # skill_points is passed the amounts of skill points the player currently 
    # has.
    #
    # The function returns 0 if the action's proficiency level is maxed. 
    # Otherwise, the function returns 1.
    # **************************************************************************
    def invest_skill_points(self, skill_points) -> int:

        #Raises a value error if skill_pints < 0.
        if skill_points < 0:
            raise ValueError

        #Displays an error message if the skill is at its maximum proficiency 
        #level.
        if self.is_skill_maxed():
            print("\nThe skill cannot be improved any further.")
            return 0
        
        if skill_points < SKILL_POINT_COST:
            print("\nYou do not have enough skill points.")
            return 1

        self._proficiency_lvl += 1

        return 2

    # **************************************************************************
    # Function to reset the current action's proficiency level.
    #
    # none:
    #
    # The function returns the number of skill points that have been invested
    # in the current skill
    # ************************************************************************** 
    def reset_proficiency_lvl(self) -> int:
        if self._proficiency_lvl == 1:
            print("\nNo skill points have been invested in this skill.")
            return 0

        #Calculates the number of skill points that have been invested in the
        #skill.
        skill_points = self._proficiency_lvl * SKILL_POINT_COST
        self._proficiency_lvl = 1  #Resets the skill proficiency level to zero.
        return skill_points


    # **************************************************************************
    # Function to display the current action's proficiency level.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display_proficiency_lvl(self):
        print("\nCurrent Skill Level: ", self._proficiency_lvl)

        return

#Interface for the SwordFighting class, which is a subclass of the Action class. 
class SwordFighting (Action):
    
    #Default constructor
    def __init__(self) -> None:
        self._sword_lvl = 1    
        
        #Calls the Action class's default constructor
        super().__init__()

    # **************************************************************************
    # Function to simulate the player's character attacking an enemy.
    #
    # none
    #
    # The function returns 0 if the player chooses the wrong action. Otherwise, 
    # the function returns the player's damage output if the player chose
    # chose the correct action.
    # **************************************************************************
    def attack(self) -> int:

        #Returns the player's calculated damage output. 
        return self._sword_lvl * self._proficiency_lvl * DAMAGE_OUTPUT

    # **************************************************************************
    # Function to simulate the player's character dodging an enemy's attack.
    #
    # none
    #
    # The function returns 0 if the character failed to dodge an attack. 
    # Otherwise, the functions 1 if the character was able to successfully
    # dodge an attack.
    # **************************************************************************
    def dodge(self) -> int:

        #Variable to represent the probability of the character failing to
        #dodge an attack. (Starting probability is 1/5).
        dodge_failure = randint(1, 5)
        dodge_index = randint(1, self._proficiency_lvl + 4)

        #Returns 0 to the calling routine if the character fails to dodge the
        #enemy's attack.
        if dodge_failure == dodge_index: 
            return 0
        
        return 1 

    # **************************************************************************
    # Function to upgrade the player's character's sword.
    #
    # param: none
    #
    # The function returns 0 if the sword is already fully upgraded, 1 if the 
    # player does not have coins to afford the upgrade, or 2 if the upgrade
    # was successful.
    # **************************************************************************
    def upgrade_sword(self, coin_pouch: int) -> int:

        #Raises a value error if skill_pints < 0.
        if coin_pouch < 0:
            raise ValueError

        #Returns 0 to the calling routine if the sword is fully upgraded.
        if self._sword_lvl == SWORD_LVL_MAX:
            return 0
         
        if coin_pouch < SWORD_UPGRADE_COST:
            return 1

        self._sword_lvl += 1   #Upgrades the sword.

        return 2
    
    # **************************************************************************
    # Function to display the sword level.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display_sword_lvl(self) -> None:
        print(f"\nSword Level: {self._sword_lvl}")
        return

        
#Interface for the Assisting class, which is a subclass of the Action class. 
class Assisting (Action):

    #Default constructor
    def __init__(self) -> None:
        self._assistance_count = 0
        super().__init__()

    #Overloaded < operator
    def __lt__(self, count: int) -> bool:
        return self._assistance_count < count

    #Overloaded >= operator 
    def __le__(self, count: int) -> bool:
        return self._assistance_count >= count

    #Overloaded < operator 
    def __gt__(self, count: int):
        return self._assistance_count < count

    #Overloaded >= operator 
    def __ge__(self, count: int):
        return self._assistance_count <= count
    
    # **************************************************************************
    # Function to allow the player to decide whether to assist an NPC with
    # a particular task.
    #
    # param: none
    #
    # The function returns 0 if the player declines to help. Otherwise, the
    # function returns a positive integer, representing the amount of coins the 
    # player will receive for providing assistance.
    # **************************************************************************
    def assist(self) -> int:
        self.generate_request()   #Randomly generates an assistance request.
        assist_choice = ' '
        reward_amount = 0

        #Reads in the player's decision.
        assist_choice = input().lower()

        #Repeatedly prompts the player to enter 'y' or 'n' until they enter a
        #valid response.
        while assist_choice != 'y' and assist_choice != 'n':
            assist_choice = input("\nPlease enter 'y' for yes or 'n' for no: ").lower()

        #Generates a random amount of coins the player will receive for
        #providing assistance.
        if assist_choice == 'y':
            reward_amount = self.generate_reward()

            #Increments the number of times the player provided assistance.
            self._assistance_count += 1  

        return reward_amount

    # **************************************************************************
    # Function to generate a random amount of coins.
    #
    # param: none
    #
    # The function returns the amount of coins generated.
    # **************************************************************************
    def generate_reward(self) -> int:
        #Generates a random amount of coins. The amount of coins generated
        #will increase as the player's proficiency level increases.
        return randint(15, 30) * self._proficiency_lvl

    # **************************************************************************
    # Function to generate a request for assistance.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def generate_request(self) -> int:
        scenario = randint(1, 5)    

        if scenario == 1:
            print("\nYou encounter a group of merchants who needs to travel to"
                  "\na nearby town but are afraid of bandits on the road.")
            
            print("\nWill you escort the merchants to their destination? (y/n): ", end='') 

        elif scenario == 2:
            print("\nYou come across a construction site in a busting town."
                  "\nYou learn that the workers require additional manpower to" 
                  "\nfinish the project on time.")
            
            print("\nWill you help the workers with the construction? (y/n): ", end='') 

        elif scenario == 3:
            print("\nYou encounter a distraught man in a village whose"
                  "\ndaughter was recently kidnapped by a group of bandits"
                  "\nThe man pleads for help in tracking down the bandits and"
                  "\nrescuing his daughter.")
            
            print("\nWill you help track down and rescue the kidnapped girl? (y/n): ", end='') 

        elif scenario == 4:
            print("\nYou stumble upon a village being terrorized by a pack of"
                  "\nferocious wolves. The villagers requests your help in"
                  "\ndriving away the wolves.")

            print("\nWill you help the villagers drive away the wolves? (y/n): ", end='') 

        elif scenario == 5:
            print("\nYou arrive in a bustling town that is preparing to host a"
                  "\na grand celebration. However, the organizers are overwhelmed"
                  "\nwith the preparations and require additional assistance to"
                  "\nto ensure the success of the event.")
                
            print("\nWill you help the organizers with the preparations? (y/n): ", end=' ') 

        return scenario

    #Overloaded the str() function to display the number of times the player has
    #provided assistance.
    def __str__(self):
        return f"You have fulfilled {self._assistance_count} help request(s)."

#Interface for the Healing, which is a subclass of the Action class. 
class Healing (Action):

    #Default constructor
    def __init__(self) -> None:
        self._healing_items = ["Healing Salve", "Healing Poultice", "Healing Potion"]
        self._inventory = array([0, 0, 0])
        super().__init__()

    # **************************************************************************
    # Function to allow the player to select a healing item in their inventory 
    # to use.
    #
    # param: none
    #
    # The function returns the amount of hp the selected healing item will 
    # restore.
    # **************************************************************************
    def apply_treatment(self) -> int:
        item_choice = 0      #Holds the selected healing item.
        restore_amount = 0   #Holds the amount of hp that will be restored.
    
        print("\nHealing items: "
              f"\n1. Healing Salve           (heals {SALVE_RESTORE} hp)"
              f"\n2. Healing Poultice        (heals {POULTICE_RESTORE} hp)"
              f"\n3. Healing Potion          (heals {POTION_RESTORE} hp)"
              f"\n4. Quit")

        #Repeatedly prompts the player to enter their choice until a valid
        #choice is entered.
        while item_choice < 1 or item_choice > 4:
            item_choice = v.read_int("\nChoose a healing item (Enter 1-4): ")

            #Displays an error message if the player entered an integer outside
            #1-4.
            if item_choice < 1 or item_choice > 4:
                print("Please enter 1-4.")
 
        os.system('cls')   #Clears the screen

        #Returns 0 to the calling routine if the player chooses to quit.
        if item_choice == 4:
            return 0

        #If the player selects "Healing Salve"...
        if item_choice == 1:

            #Displays an error message if there are zero healing salves in 
            #the player's inventory.
            if self._inventory[0] == 0:
                print("\nYou are out of healing salves.")

            #Otherwise, saves the amount of hp to be restored and decrement
            #the number of healing salves in the player's inventory by 1. 
            else:
                restore_amount = SALVE_RESTORE
                self._inventory[0] -= 1

        #If the player selects "Healing Poultice"...
        elif item_choice == 2:

            #Displays an error message if there are zero healing poultices in 
            #the player's inventory.
            if self._inventory[1] == 0:
                print("\nYou are out of healing poultices.")

            #Otherwise, saves the amount of hp to be restored and decrement
            #the number of healing poultices in the player's inventory by 1. 
            else:
                restore_amount = POULTICE_RESTORE
                self._inventory[1] -= 1

        #If the player selects "Healing Potion"...
        else:
            #Displays an error message if there are zero healing potions in 
            #in the player's inventory.
            if self._inventory[2] == 0:
                print("\nYou are out of healing potions.")

            #Otherwise, saves the amount of hp to be restored and decrement
            #the number of healing potions in the player's inventory by 1. 
            else:
                restore_amount = POTION_RESTORE
                self._inventory[2] -= 1

        restore_amount *= self._proficiency_lvl

        if restore_amount != 0:
            print(f"\n{restore_amount} hp restored.")

        return restore_amount 

    # **************************************************************************
    # Function to allow the player to purchase healing items.
    #
    # param: none
    #
    # The function returns the remaining amount of coins in the player's
    # coin_pouch.
    # **************************************************************************
    def purchase_healing_items(self, coin_pouch: int) -> int:

        #Raises a value error if coin_pints < 0.
        if coin_pouch < 0:
            raise ValueError
        
        item_choice = 0      #Holds the selected healing item.
        quantity = -1        #Holds the number of the selected item to purchase.

        #Tracks whether the player has enough coins for their purchase.
        not_enough_coins = False

        #Displays the available healing items that can be purchased along with
        #prices.
        print(f"\nHealing items: "
              f"\n1. Healing Salve      {SALVE_PRICE} coins"
              f"\n2. Healing Poultice   {POULTICE_PRICE} coins"
              f"\n3. Healing Potion     {POTION_PRICE} coins"
              f"\n4. Quit")

        #Repeatedly prompts the player to enter their choice until a valid
        #choice is entered.
        while item_choice < 1 or item_choice > 4:
            item_choice = v.read_int("\nChoose a healing item (Enter 1-4): ")

            #Displays an error message if the player entered an integer outside
            #1-4.
            if item_choice < 1 or item_choice > 4:
                print("Please enter 1-4.")

        os.system('cls')   #Clears the screen

        #Returns 0 to the calling routine if the player chooses to quit.
        if item_choice == 4:
            return 0

        #Repeatedly prompts the player to indicate the quantity of the
        #selected item they wish to purchase until they enter a nonnegative
        #integer.
        while quantity < 0:
            quantity = v.read_int(f"\nHow many "
                                  f"{self._healing_items[item_choice - 1].lower()}"
                                  f"(s) would you like to purchase: ")

            #Displays an error message if the player entered negative value.                
            if quantity < 0:
                print("Please enter a nonnegative integer.")

        #If the player selects "Healing Salve"...
        if item_choice == 1:

            #If the player does not have enough coins to purchase the quantity
            #specified.
            if quantity * SALVE_PRICE > coin_pouch:
                not_enough_coins = True 

            #Otherwise, process the purchase.
            else:
                coin_pouch -= quantity * SALVE_PRICE

        #If the player selects "Healing Poultice"...
        elif item_choice == 2:

            #If the player does not have enough coins to purchase the quantity
            #specified.
            if quantity * POULTICE_PRICE > coin_pouch:
                not_enough_coins = True

            #Otherwise, process the purchase.
            else:
                coin_pouch -= quantity * POULTICE_PRICE

        #If the player selects "Healing Potion"...
        elif item_choice == 3:

            #If the player does not have enough coins to purchase the quantity
            #specified.
            if quantity * POTION_PRICE > coin_pouch:
                not_enough_coins = True

            #Otherwise, process the purchase.
            else:
                coin_pouch -= quantity * POTION_PRICE

        #Displays an error message if the player does not have coins to make 
        #purchase.
        if not_enough_coins:
            print("\nYou do not have enough coins!")

        #Adds the healing items to the player's inventory.
        else:
            print("\nPurchase successful.")
            self._inventory[item_choice - 1] += quantity

        return coin_pouch

    # **************************************************************************
    # Function to allow the player to sell their healing items for coins.
    #
    # param: none
    #
    # The function returns the number of coins the player will receive from 
    # selling their healing items.
    # **************************************************************************   
    def sell_healing_items(self): 
        item_choice = 0      #Holds the selected healing item.
        quantity = -1        #Holds the number of the selected item to purchase.
        invalid_quantity = False
        profit = 0

        #Displays the quantity of each healing item in the player's inventory.
        print(f"\nHealing items: "
              f"\n1. Healing Salve       x{self._inventory[0]}"
              f"\n2. Healing Poultice    x{self._inventory[1]}"
              f"\n3. Healing Potion      x{self._inventory[2]}"
              f"\n4. Quit")

        #Repeatedly prompts the player to enter their choice until a valid
        #choice is entered.
        while item_choice < 1 or item_choice > 4:
            item_choice = v.read_int("\nChoose a healing item (Enter 1-4): ")

            #Displays an error message if the player entered an integer outside
            #1-4.
            if item_choice < 1 or item_choice > 4:
                print("Please enter 1-4.")

        #Returns 0 to the calling routine if the player chooses to quit.
        if item_choice == 4:
            return 0

        #Repeatedly prompts the player to indicate the quantity of the
        #selected item they wish to sell until they enter a nonnegative
        #integer.
        while quantity < 0:
            quantity = v.read_int(f"\nHow many "
                                  f"{self._healing_items[item_choice - 1].lower()}"
                                  f"(s) would you like to sell: ")

            #Displays an error message if the player entered negative value.                
            if quantity < 0:
                print("Please enter a nonnegative integer.")

        os.system('cls')   #Clears the screen

        #Displays an error message if the player is attempting to sell more of 
        #the selected healing item than what is in their inventory.
        if self._inventory[item_choice - 1] - quantity < 0:
            print(f"\nYou do not have enough {self._healing_items[item_choice - 1].lower()}"
                  f"(s) to sell.")
            invalid_quantity = True

        #Otherwise, subtracts the quantity of the healing items the player wish to
        #sell from their inventory.
        else:
            self._inventory[item_choice - 1] -= quantity

        if invalid_quantity:
            return 0

        #Records the number of coins the player will receive from selling the 
        #selected healing item.
        if item_choice == 1:
            profit = quantity * SALVE_PRICE

        elif item_choice == 2:
            profit = quantity * POULTICE_PRICE

        elif item_choice == 3:
            profit = quantity * POTION_PRICE
 
        return profit

    # **************************************************************************
    # Function to display the quantity of each healing item in the player's
    # inventory.
    #
    # param: none
    #
    # return: none
    # **************************************************************************   
    def view_inventory(self) -> None:
        index = 0

        print("\nInventory: ")
        while index < len(self._healing_items):
            print(f"{self._healing_items[index]}: {self._inventory[index]}")
            index += 1  

        return 
