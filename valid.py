# *****************************************************************************
# Author:      Huan Nguyen
# Date:        06/1/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   valid.py
# Purpose:     This file contains functions to read in and validate for a 
#              specific data type.
# *****************************************************************************

# **************************************************************************
# Function to read in an integer.
#
# param: none
#
# The function returns the integer that was read in.
# **************************************************************************
def read_int(prompt = "Please enter an integer"):
    num = 0 
    valid = False

    #Repeatedly prompts the user to enter an integer if they enter a 
    #non-integer value.
    while not valid:

        #Attempts to convert the the user input to an integer.
        try:
            num = int(input(prompt))
            valid = True

        #Throws an exception if the user enters a non-integer value.
        except:
            print("Invalid input type. Please enter an integer")

    return num

