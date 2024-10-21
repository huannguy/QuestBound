# ******************************************************************************
# Author:      Huan Nguyen
# Date:        06/5/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   game.py
# Purpose:     This file contains the interfaces for the Game class that will
#              manage the operations of the game.
# ******************************************************************************
import character
import valid as v
import os

BOSS_HP = 1000

class Game:

    #Default constructor
    def __init__(self) -> None:
        self._hero = character.Character()
        self._turn = 1

    # **************************************************************************
    # Function to display information about the game.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display_game_info(self) -> None:
        print("\nQuestbound is a fantasy quest game where players embark on an"
              "\nepic journey to defeat the dark sorceress Morwenna whose"
              "\nmalevolent influence threatens the entire realm. The game was"
              "\ndesigned to introduce players to beginner-level programming"
              "\nconcepts. A the player progresses through the game, they will" 
              "\nencounter situations that will help familiarize them with"
              "\nprogramming concepts, specifically executable statements,"
              "\nconditional statements, and loops.")
        
        return

    # **************************************************************************
    # Function to read in the character's information.
    #
    # param: none
    #
    # return: none.
    # **************************************************************************
    def read_character_info(self) -> None:
        self._hero.read_name()
        os.system('cls')   #Clears the screen

        return
    
    # **************************************************************************
    # Function to display game instructions.
    #
    # param: none
    #
    # return: none.
    # **************************************************************************
    def display_instructions(self) -> None:
        print("\nThe objective of the game is to reach Morwenna's lair within"
              "\n20 turns. Choosing the \"Proceed Ahead\" option will progress"
              "\nthe game state to the next turn. There are three types of"
              "\nactions the player can partake in: combat, assisting, and"
              "\nhealing. The combat mechanic represents loops. As the player"
              "\nprogresses through the game they may encounter hostile enemies"
              "\nthat will need to be defeated. During skirmishes with an enemy"
              "\nopponents, a series of instructions will appear on the screen"
              "\nthat the player will need to follow in order to defeat the"
              "\nememy. These instructions will continue to appear until the"
              "\nthe enemy has been defeated or the player has been defeated."
              "\nThe assisting mechanic represents conditional statements. As"
              "\nthe player progresses through the game, they may encounter"
              "\nscenarios where they are given the choice of providing"
              "\nassistance to an NPC or NPCs in exchange for coins at the"
              "\ncost of an additional turn or decline the request. The healing"
              "\nmechanic represents executable statements. During battles,"
              "\nthere is a chance for the player to lose hp if they fail to"
              "\ndodge an attack. If the player's character's hp falls to zero" 
              "\nat any point during the game, they will lose the game. As such," 
              "\nthe player will need to periodically heal themselves with"
              "\nhealing items to avoid this scenario. The player cannot heal"
              "\nduring a battle.")
        
        return

    # **************************************************************************
    # Function to manage the main menu.
    #
    # param: none
    #
    # The function returns 0 if the player chooses to quit the game, 1 if the
    # player's character's health falls to zero, 2 if the player fails to 
    # reach Morwenna's lair within 20 turns, or 3 if the player successfully
    # reached Morwenna's lair within 20 turns.
    # **************************************************************************
    def manage_game(self) -> int:
        action_choice = 0
        zero_health = False
        destination_reached = False
        engage_boss_choice = False

        #Repeats until 20 turns have passed, or the player's character dies, or
        #the player chooses to engage Morwenna, or the player chooses to
        #quit.
        while self._turn < 20 and not zero_health and not engage_boss_choice and action_choice != 8:

            #Displays the turn number and the remaining distance the player has to
            #cover to reach Morwenna's lair.
            print("\nTurn #", self._turn)
            self._hero.display_remaining_distance()

            #Checks if the player has reached Morwenna's lair.
            destination_reached = self._hero.is_at_destination()

            #Informs the player they have reached Morwenna's lair.
            if destination_reached:
                print("\nYou have reached Morwenna's lair. Ensure you are"
                      "\nfully prepared before proceeding. Once you"
                      "\nhave engaged Morwenna, you will not be able to"
                      "\nupgrade your weapons, stats, or heal. Best of luck!")

            #Displays a menu of possible options for the main menu.
            print("\nActions:"
                  "\n1. Proceed Ahead"
                  "\n2. View Character Profile"
                  "\n3. Combat"
                  "\n4. Assist"
                  "\n5. Heal"
                  "\n6. Earnings Log"
                  "\n7. View Instructions"
                  "\n8. Quit Game")
            
            action_choice = v.read_int("\nChoose an action (enter 1-8): ")
            os.system('cls')   #Clears the screen

            #Reminds the player of the valid choices if the they entered
            #an integer less than 1 or greater than 8.
            if action_choice < 1 or action_choice > 8:
                print("\nPlease enter 1-8.")

            #If the player chooses "Proceed Ahead"...
            if action_choice == 1:

                #Progresses the game normally if the player has not
                #reached Morwenna's lair.
                if not destination_reached:
                    self._turn = self._hero.proceed_ahead(self._turn)

                    if self._turn == 0:
                        zero_health = True

                #Assign engage_boss_choice to True if the player
                #reached Morwenna's lair.
                else:
                    engage_boss_choice = True

            #Displays the character's profile.
            elif action_choice == 2:
                self._hero.display_profile()

            #Displays the Combat menu.
            elif action_choice == 3:
                while self._hero.manage_combat() != 6:
                    pass

            #Displays the Assist menu.
            elif action_choice == 4:
                while self._hero.manage_assisting() != 5:
                    pass

            #Displays the Heal menu if the player chooses "Heal".
            elif action_choice == 5:
                while self._hero.manage_healing() != 8:
                    pass

            #Displays the earnings log menu.
            elif action_choice == 6:
                while self._hero.manage_earnings_log() != 6:
                    pass

            #Displays the game instructions.
            elif action_choice == 7:
                self.display_instructions()
                while input("\nHit ENTER to continue. ") != "":
                    pass
                os.system('cls')   #Clears the screen


        #Returns 0 to the calling routine if the player chooses
        #to quit the game. 
        if action_choice == 8:
            return 0

        #Returns 1 to the calling routine if the player's character
        #falls to zero.
        if zero_health:
            return 1
        
        #Returns 2 to the calling routine if the player failed
        #to make it to Morwenna's lair within 20 turns.
        if self._turn > 20:
            return 2

        return 3

    # **************************************************************************
    # Function to manage the Morwenna boss fight.
    #
    # param: none
    #
    # The function returns 0 if the player is defeated. Otherwise, the function
    # returns 1 if the player was able to defeat Morwenna.
    # **************************************************************************
    def manage_boss_fight(self) -> int:
        print("\nYou have engaged Morwenna!")

        if self._hero.simulate_combat(BOSS_HP) == 0:
            return 0
        
        return 1



