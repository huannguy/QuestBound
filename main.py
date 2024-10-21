# *****************************************************************************
# Author:      Huan Nguyen
# Date:        06/1/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   main.py
# Purpose:     This file contains the main() function that will manage the flow
#              of the game.
# *****************************************************************************
import os
import game
import valid as v

def main():
    quest_bound = game.Game()
    result = 0

    #Introduces the player to the game.
    print("\nWelcome to Questbound!")

    quest_bound.display_game_info()
    quest_bound.read_character_info()

    os.system('cls')

    quest_bound.display_instructions()
    while input("\nHit ENTER to continue. ") != "":
        pass
    
    os.system('cls')   #Clears the screen

    #Starts the game.
    result = quest_bound.manage_game()

    #Displays the following message if the player's character's
    #health falls to zero.
    if result == 1:
        print("\nYou succumbed to your injuries. Game over!")

    #Displays the following message if the player's fails to reach
    #Morwenna's lair within 20 turns.
    elif result == 2:
        print("\nYou failed to reached Morwenna's lair in time. Game over!")

    #If the player has decide to engage Morwenna...
    elif result == 3:

        #Displays the following message if the player was defeated.
        if quest_bound.manage_boss_fight() == 0:
            print("\nYou failed to defeat Morwenna. Game over!")

        #Displays the following message if the player defeated Morwenna.
        else:
            print("\nCongratulations! You successfully slew the wicked"
                  "\nsorceress Morwenna and saved the realm from doom!")
 
    print("\nThank you for playing QuestBound! See you again soon!")

if __name__ == "__main__":
    main()
