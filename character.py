# ******************************************************************************
# Author:      Huan Nguyen
# Date:        06/2/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   character.py
# Purpose:     This file contains the interfaces for the Character class which
#              represents the player's character.
# ******************************************************************************
from random import randint
import os
import time
import hierarchy
import tree
import valid as v

STARTING_HP = 90
BASE_ENEMY_HP = 50
STARTING_SKILL_POINTS = 5
STARTING_COIN_AMOUNT = 10
DESTINATION = 100

class Character:
    #Constructor with arguments
    def __init__(self) -> None:
        self._name = ""
        self._position = 0
        self._hp = STARTING_HP
        self._skill_points = STARTING_SKILL_POINTS
        self._coin_pouch = STARTING_COIN_AMOUNT
        self._earnings_log = tree.Tree()
        self._combat = hierarchy.SwordFighting()
        self._assisting = hierarchy.Assisting()
        self._healing = hierarchy.Healing()

    # **************************************************************************
    # Function to allow the the player to provide the name of their character.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def read_name(self) -> None:
        info_is_correct = 'n'

        #Repeatedly prompts the player to enter the name of their character
        #until they indicate the name they entered is correct.
        while info_is_correct == 'n':


            self._name = input("\nEnter the name of your character: ")

            #Repeatedly prompts the player to enter the name of their
            #character until they enter a nonempty string.
            while self._name == "":
                print("Please enter a nonempty string")
                self._name = input("\nEnter the name of your character: ")

            print(f"\nName: {self._name}")

            info_is_correct = input("\nIs this correct? (y/n): ").lower()

            #Repeatedly prompts the player to type 'y' or 'n' to indicate
            #whether the name they entered is correct until they enter
            #a valid response.
            while info_is_correct != 'y' and info_is_correct != 'n':
                info_is_correct = input("\nEnter 'y' for yes or 'n' for no: ")

        return 

    # **************************************************************************
    # Function to display the character's profile
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display_profile(self) -> None:
        print(f"\nCharacter Profile: "
              f"\nName: {self._name}"
              f"\nHP: {self._hp}"
              f"\nSkill Points: {self._skill_points}"
              f"\nCoin Pouch: {self._coin_pouch} coins")
        
        return
        
    # **************************************************************************
    # Function to display the remaining distance to Morwenna's lair.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display_remaining_distance(self) -> None:
        print(f"\nRemaining distance: {DESTINATION - self._position} mi")

        return
    
    # **************************************************************************
    # Function to check if the player has reached Morwenna's lair.
    #
    # param: none
    #
    # The function returns false if the player has not yet reached Morwenna's
    # lair. Otherwise, the function returns true if they have.
    # **************************************************************************
    def is_at_destination(self) -> bool:
        return self._position == DESTINATION

    # **************************************************************************
    # Function to advance to the next turn.
    #
    # param: none
    #
    # The function returns 0 if the player was defeated in combat. Otherwise,
    # the function returns the next turn number.
    # **************************************************************************
    def proceed_ahead(self, turn) -> int:
        event = randint(0, 1)   #Randomly generates one of two possible events.

        #Simulates the player encountering a hostile enemy.
        if turn > 1 and event == 0:
            print("\nAn enemy appears!")
            print("\nThis situation represents a loop. The battle will persist"
                  "\nuntil either the player or the enemy is defeated.")

            #Determines the HP of the enemy opponent. Enemies encountered later will
            #have higher HP than those encountered at the beginning.
            enemy_hp = BASE_ENEMY_HP + turn * 5

            if self.simulate_combat(enemy_hp) == 0:
                return -1

            #Otherwise, informs the player they defeated the enemy and
            #reward them with five skill points. 
            else:
                print("\nYou successfully defeated the enemy opponent.")
                self._skill_points += 5

        #Simulates the player encountering an NPC or group of NPC's who 
        #are in need of help.
        elif event == 1:
            print("\nThis situation represents a conditional statement or"
                  "\ndecision. The result will be different depending on"
                  "\nyour decision.")

            reward_amount = self._assisting.assist()

            #If the player chooses to provide assistance...
            if reward_amount:
                print("\nYou received", reward_amount, "coins as a reward!")

                #Rewards the player with coins for assisting.
                self._coin_pouch += reward_amount   

                self._earnings_log.insert(reward_amount, turn)

                turn += 1   #Increases the turn number by 1.

            else:
                print("\nYou declined the request.")

        if self._hp <= 0:
            return 0
 
        turn += 1

        self._position += 10
        
        return turn

    # **************************************************************************
    # Function to manage the default Combat menu.
    #
    # param: none
    #
    # The function returns the player's action choice.
    # **************************************************************************
    def manage_combat(self) -> int:
        action_choice = 0

        #Displays a menu of possible options for the Combat menu.
        print("\n~~~~~~~~~~~~~~~~~~~~Combat~~~~~~~~~~~~~~~~~~~~~"
              "\n1. Increase proficiency (costs 10 skill points)"
              "\n2. Reset Proficiency Level"
              "\n3. View Proficiency Level"
              f"\n4. Upgrade Sword        (costs {hierarchy.SWORD_UPGRADE_COST} coins)"
              "\n5. View Sword Level"
              "\n6. Quit Menu")

        #Repeatedly prompts the player to select an action from the Combat menu
        #until they choose a valid choice.
        while action_choice < 1 or action_choice > 6:
            action_choice = v.read_int("\nChoose an action (Enter 1-6): ")

            #Displays an error message if the player entered an integer outside
            #1-5.
            if action_choice < 1 or action_choice > 6:
                print("Please enter 1-6.")

        os.system('cls')   #Clears the screen

        #If the player chooses to increase their character's combat proficiency...
        if action_choice == 1:

            #Subtracts five skill points from the player's skill points amount 
            #if the operation was successful.
            if self._combat.invest_skill_points(self._skill_points) == 2:
                print("\nCombat proficiency has increased one level.")
                self._skill_points -= 5

        #If the player chooses to reset their character's combat proficiency...
        elif action_choice == 2:
            self._skill_points = self._combat.reset_proficiency_lvl()

        #If the player chooses to view their character's combat proficiency level...
        elif action_choice == 3:
            self._combat.display_proficiency_lvl()

        #If the player chooses to upgrade their character's sword...
        elif action_choice == 4:

            result = self._combat.upgrade_sword(self._coin_pouch)

            #Displays the following error message if the player does not have
            #coins to afford the sword upgrade.
            if result == 0:
                print("\nThe sword cannot be upgraded any further.")

            #Displays the following error message if the player does not have
            #coins to afford the sword upgrade.
            if result == 1:
                print("\nYou do not have coins to afford the upgrade.")

            #Otherwise, subtract 10 coins from the player's coin pouch if the
            #upgrade was successful.
            if result == 2:
                print("\nUpgrade successful.")
                self._coin_pouch -= hierarchy.SWORD_UPGRADE_COST

        #If the player chooses to view the sword level...
        elif action_choice == 5:
            self._combat.display_sword_lvl()

        return action_choice

    # **************************************************************************
    # Function to simulate the player facing off against an hostile enemy.
    #
    # enemy_hp is passed the enemy's hp as determined by the calling routine.
    #
    # The function returns 0 if the player was defeated. Otherwise, the 
    # function returns 1 if the enemy was defeated.
    # **************************************************************************
    def simulate_combat(self, enemy_hp):

        #Repeats attack sequence until either the player or the enemy opponent is
        #defeated.
        while self._hp > 0 and enemy_hp > 0:
            action_type = randint(0, 1)   #Determines the assigned action type.
            assigned_action = 0
            action_choice = 0
            
            print("\nCharacter HP:", self._hp,
                  "\nEnemy HP:", enemy_hp)

            #If action_type is 0... 
            if action_type == 0:

                #Determines the assigned swing direction.
                swing_direction = randint(0, 1)

                #Instructs the player to swing left if the swing_direction
                #is 0.
                if swing_direction == 0:
                    print("\nSwing left!")
                    assigned_action = 1
                    
                #Instructs the player to swing right if the swing_direction
                #is 1.
                else:
                    print("\nSwing right!")
                    assigned_action = 2
        
            #If action_type is 0... 
            else:
                #Instructs the player to dodge.
                print("\nDodge!")
                assigned_action = 3

            #Displays possible actions the player may take during the battle.
            print("\nPossible actions: "
                  "\n1. Swing left"
                  "\n2. Swing right"
                  "\n3. Dodge")

            #Reads in the player's action choice. 
            action_choice = v.read_int("\nChoose an action: (Enter 1-3): ")
            os.system('cls')

            #If the player was supposed to attack the enemy...
            if action_type == 0:

                #If the player did not choose the correct attack maneuver...
                if action_choice != assigned_action:
                    print("\nEnemy took zero damage!")

                #Otherwise, subtract from the enemy's hp if the player chose the 
                #correct attack maneuver.
                else:
                    enemy_hp -= self._combat.attack()

            #If the player was instructed to dodge...            
            else:
                dodge_result = 0

                #Determines the character's dodge result. 
                dodge_result = self._combat.dodge()

                #Displays the following error message and subtracts 10
                #from the player's hp if either the player choose the
                #correct action or their dodge_result is 0.
                if action_choice != 3 or dodge_result == 0:
                    print("\nFailed to dodge. Sustained damage")
                    self._hp -= 10

                #Informs the player their character was able to dodge the 
                #enemy's attack if dodge_result is 1. 
                elif dodge_result == 1:
                    print("\nAvoided the attack!")
 
        #Returns 0 to the calling routine if the player was
        #defeated.
        if self._hp == 0:
            return 0

        else:
            return 1

    # **************************************************************************
    # Function to manage the Assist menu.
    #
    # param: none
    #
    # The function returns the player's action choice.
    # **************************************************************************
    def manage_assisting(self) -> int:
        action_choice = 0

        #Displays a menu of possible options for the Assist menu.
        print("\n~~~~~~~~~~~~~~~~~~~~Assist~~~~~~~~~~~~~~~~~~~~~"
              "\n1. Increase proficiency (costs 10 skill points)"
              "\n2. Reset Proficiency Level"
              "\n3. View Proficiency Level"
              "\n4. View Assistance Count"
              "\n5. Quit Menu")

        #Repeatedly prompts the player to select an action from the Assist menu
        #until they choose a valid choice.
        while action_choice < 1 or action_choice > 5:
            action_choice = v.read_int("\nChoose an action (Enter 1-5): ")

            #Displays an error message if the player entered an integer outside
            #1-5.
            if action_choice < 1 or action_choice > 5:
                print("Please enter 1-5.")

        os.system('cls')   #Clears the screen

        #If the player chooses to increase their character's assisting proficiency...
        if action_choice == 1:

            #Subtracts five skill points from the player's skill points amount 
            #if the operation was successful.
            if self._assisting.invest_skill_points(self._skill_points) == 2:
                print("\nAssisting proficiency has increased one level.")
                self._skill_points -= 5

        #If the player chooses to reset their character's assisting proficiency level
        #to zero...
        elif action_choice == 2:
            self._skill_points = self._assisting.reset_proficiency_lvl()

        #If the player chooses to view their character's assisting proficiency level...
        elif action_choice == 3:
            self._assisting.display_proficiency_lvl()

        #If the player chooses to view the number of times they provided assistance...
        elif action_choice == 4:
            print(f"\n{self._assisting}")

        return action_choice

    # **************************************************************************
    # Function to manage the Heal menu
    #
    # param: none
    #
    # The function returns the player's action choice.
    # **************************************************************************
    def manage_healing(self) -> int:
        action_choice = 0

        print("\nThese actions represent executable statements.")

        #Displays a menu of possible options for the Heal menu.
        print("\n~~~~~~~~~~~~~~~~~~~~~Heal~~~~~~~~~~~~~~~~~~~~~~"
              "\n1. Increase proficiency (costs 10 skill points)"
              "\n2. Reset Proficiency Level"
              "\n3. View Proficiency Level"
              "\n4. Apply Treatment"
              "\n5. Purchase Healing Items"
              "\n6. Sell Healing Items"
              "\n7. View Inventory"
              "\n8. Quit Menu")

        #Repeatedly prompts the player to select an action from the Heal menu
        #until they choose a valid choice.
        while action_choice < 1 or action_choice > 8:
            action_choice = v.read_int("\nChoose an action (Enter 1-8): ")

            #Displays an error message if the player entered an integer outside
            #1-8.
            if action_choice < 1 or action_choice > 8:
                print("Please enter 1-8.")
 
        os.system('cls')   #Clears the screen

        #If the player chooses to increase their character's healing proficiency...
        if action_choice == 1:

            #Subtracts five skill points from the player's skill points amount 
            #if the operation was successful.
            if self._healing.invest_skill_points(self._skill_points) == 2:
                print("\nHealing proficiency has increased one level.")
                self._skill_points -= 5

        #If the player chooses to reset their character's healing proficiency level
        #to zero...
        elif action_choice == 2:
            self._skill_points = self._healing.reset_proficiency_lvl()

        #If the player chooses to view their character's healing proficiency level.
        elif action_choice == 3:
            self._healing.display_proficiency_lvl()

        #If the player chooses to heal their character's hp...
        elif action_choice == 4:
            if self._hp == STARTING_HP:
                print("\nYou are already at full health.")

            else:
                print(f"\nHP: {self._hp}")
                self._hp += self._healing.apply_treatment()

            if self._hp > STARTING_HP:
                self._hp = STARTING_HP

        #If the player chooses to purchase healing items...
        elif action_choice == 5:
            print(f"\nCoin Pouch: {self._coin_pouch}")
            self._coin_pouch = self._healing.purchase_healing_items(self._coin_pouch)

        #If the player chooses to sell their healing items....
        elif action_choice == 6:
            self._coin_pouch += self._healing.sell_healing_items()

        #If the player chooses to view their healing items inventory.
        elif action_choice == 7:
            self._healing.view_inventory()

        return action_choice


    # **************************************************************************
    # Function to manage the earnings log menu.
    #
    # param: none
    #
    # The function returns the player's action choice.
    # **************************************************************************
    def manage_earnings_log(self):
        action_choice = 0
        amount_to_find = 0
        result = 0

        print("\nThe earnings log tracks the amount of coins the player earns"
              "\nfrom completing help requests from NPCs. It does not track"
              "\nthe profit made from selling healing items.")

        #Displays a menu of possible options for the earnings log menu.
        print("\n~~~~~~~~~~~~~~~~~~~~~Earnings Log~~~~~~~~~~~~~~~~~~~~~~"
              "\n1. View Individual Earnings"
              "\n2. View Total Earnings"
              "\n3. View Average Earnings"
              "\n4. Look Up an Earning Amount"
              "\n5. Remove Entry"
              "\n6. Quit Menu")

        #Repeatedly prompts the player to select an action from the Heal menu
        #until they choose a valid choice.
        while action_choice < 1 or action_choice > 6:
            action_choice = v.read_int("\nChoose an action (Enter 1-6): ")

            #Displays an error message if the player entered an integer outside
            #1-6.
            if action_choice < 1 or action_choice > 6:
                print("Please enter 1-6.")
 
        os.system('cls')   #Clears the screen

        #Displays all individual earning amounts
        if action_choice == 1:
            if self._earnings_log.display() == 0: 
                print("\nYou have not completed any help requests.")


        #Displays the total earning.
        elif action_choice == 2:
            total = self._earnings_log.find_sum()

            if total == 0: 
                print("\nYou have not completed any help requests.")

            else:
                print("\nTotal Earnings:", total, "coins")

        #Displays the average earning per help request completed.
        elif action_choice == 3:
            average = self._earnings_log.find_average()

            if average == -1:
                print("\nYou have not completed any help requests.")

            else:
                print(f"\nAverage Earnings Per Help Request: {average:.2f} coins.")

        #Retrieve a specific earning entry.
        elif action_choice == 4:

            #Repeatedly prompts the player to enter an earning amount to search for 
            #until they enter a valid amount.
            while amount_to_find < 15:
                amount_to_find = v.read_int("\nEnter the earning amount you wish to search for: ")

                if amount_to_find < 15:
                    print("\nPlease enter a value greater than or equal to 15.")

            result = self._earnings_log.retrieve(amount_to_find)

            if result == -1:
                print("\nYou have not earned any coins.")

            elif result == 0:
                print("\nThe specified amount could not be found.")

        #Removes a specific earning entry.
        elif action_choice == 5:

            #Repeatedly prompts the player to enter an earning amount to remove from
            #the earnings log until they enter a valid amount.
            while amount_to_find < 15:
                amount_to_find = v.read_int("\nEnter the earning amount you wish to remove: ")

                if amount_to_find < 15:
                    print("\nPlease enter a value greater than or equal to 15.")

            result = self._earnings_log.remove(amount_to_find)

            if result == -1:
                print("\nYou have not completed any help requests.")

            elif result == 0:
                print("\nThe specified amount could not be found.")

            else:
                print("\nThe amount has been removed from your earnings log.")

        return action_choice

            


        
