# *****************************************************************************
# Author:      Huan Nguyen
# Date:        06/5/2024
# Class:       CS 302
# Project:     Programming Assignment #4/5
# File Name:   main.py
# Purpose:     This file contains the interfaces for the Node and Tree classes.
# *****************************************************************************
from typing import Tuple

#Interface for the Node class that will represent a node in a binary
#search tree.
class Node:

    #Default constructor
    def __init__(self, coin_amount: int, turn: int) -> None:

        if coin_amount < 15 or turn < 1:
            raise ValueError
        
        self.__coins_earned = coin_amount
        self.__turn = turn
        self.__left = None
        self.__right = None

    #Function to overload the < operator the Node class.
    def __lt__(self, op2) -> bool:
        return self.__coins_earned < op2

    #Function to overload the > operator the Node class.
    def __gt__(self, op2) -> bool:
        return self.__coins_earned > op2
    
    #Function to overload the == operator the Node class.
    def __eq__(self, op2) -> bool:
        return self.__coins_earned == op2

    #Function to overload the str operator the Node class.
    def __str__(self) -> str:
        return f"You earned {self.__coins_earned} coins on turn #{self.__turn}."

    # **************************************************************************
    # Function to display the coin earnings amount.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def display(self) -> None:
        print(self.__coins_earned, end=' ')
        return 

    # **************************************************************************
    # Function to overwrite the current data with new data.
    #
    # param: none
    #
    # return: none
    # **************************************************************************
    def update_data(self, coin_amount: int, turn: int) -> None:
        self.__coins_earned = coin_amount
        self.__turn = turn
        return 

    # **************************************************************************
    # Function to check if the node's left child reference is not None.
    #
    # param: none
    #
    # The function returns false if the node's left child reference is None. 
    # Otherwise, the function returns true if the node's left child reference
    # is not None.
    # **************************************************************************
    def has_left(self) -> bool:
        return self.__left != None

    # **************************************************************************
    # Function to check if the node's right child reference is not None.
    #
    # param: none
    #
    # The function returns false if the node's right child reference is None. 
    # Otherwise, the function returns true if the node's right child reference
    # is not None.
    # **************************************************************************
    def has_right(self) -> bool:
        return self.__right != None

    # **************************************************************************
    # Function to set the node's left child reference to a new value.
    #
    # new_left is passed the value of the new left child reference.
    #
    # return: none
    # **************************************************************************
    def set_left(self, new_left: 'Node') -> None:
        self.__left = new_left
        return 

    # **************************************************************************
    # Function to set the node's right child reference to a new value.
    #
    # new_right is passed the value of the new right child reference.
    #
    # return: none
    # **************************************************************************
    def set_right(self, new_right: 'Node') -> None:
        self.__right = new_right
        return 

    # **************************************************************************
    # Function to return the node's left child reference.
    #
    # param: none
    #
    # The function returns the node's left child reference.
    # **************************************************************************
    def get_left(self) -> 'Node':
        return self.__left

    # **************************************************************************
    # Function to return the node's right child reference.
    #
    # param: none
    #
    # The function returns the node's right child reference.
    # **************************************************************************
    def get_right(self) -> 'Node':
        return self.__right

    # **************************************************************************
    # Function to return the coin earnings amount and turn number.
    #
    # param: none
    #
    # The function returns the coin earnings amount and turn number
    # ************************************************************************** 
    def get_data(self) -> int:
        return self.__coins_earned, self.__turn


#Interface for the Tree class that will represent a binary search tree.
class Tree:
    #Default constructor.
    def __init__(self) -> None:
        self.__root = None

    # **************************************************************************
    # Wrapper function to insert a new data item into a BST.
    #
    # data is passed the amount of coins the player has earned after providing
    # assistance.
    #
    # The function returns 1.
    # ************************************************************************** 
    def insert(self, coin_amount: int, turn: int) -> int:
        if coin_amount < 15 or turn < 1:
            raise ValueError

        self.__root = self.__insert_recursive(self.__root, coin_amount, turn)

        return 1

    # **************************************************************************
    # Recursive function to insert a new data item into a BST.
    #
    # root is passed an object reference to the node being traversed.
    #
    # coin_amount is passed the amount of coins the player has earned after 
    # providing assistance.
    #
    # turn is passed the turn number corresponding to the turn in which the
    # player completed a help request.
    #
    # The function returns the newly created node.
    # ************************************************************************** 
    def __insert_recursive(self, root: Node, coin_amount: int, turn: int) -> Node:
        #Inserts the data item as a leaf.
        if root == None:
            root = Node(coin_amount, turn)
            return root

        #Raises a value error if coin_amount is less than 15 or turn is less
        #than 1. 
        if coin_amount < 15 or turn < 1:
            raise ValueError

        #Traverses the left subtree if the data item to be inserted is less than
        #the data in the current node.
        if coin_amount < root:
            root.set_left(self.__insert_recursive(root.get_left(), coin_amount, turn))

        #Traverses the right subtree if the data item to be inserted is greater 
        #than or equal to the data in the current node.
        else:        
            root.set_right(self.__insert_recursive(root.get_right(), coin_amount, turn))

        return root

    # **************************************************************************
    # Wrapper function to display the data in the BST in sorted order.
    #
    # param: none
    #
    # The function returns the number of data items displayed.
    # ************************************************************************** 
    def display(self) -> int:

        #Returns 0 to the calling routine if the BST is empty.
        if self.__root == None:
            return 0

        return self.__display_recursive(self.__root)

    # **************************************************************************
    # Recursive function to display the data in the BST in sorted order.
    #
    # root is passed an object reference to the node being traversed.
    #
    # The function returns the number of data items displayed.
    # ************************************************************************** 
    def __display_recursive(self, root: Node) -> int:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0

        count = 0

        #Traverses the left subtree.
        count += self.__display_recursive(root.get_left())

        #Displays the data in the current node.
        root.display()

        #Traverses the left subtree.
        count += self.__display_recursive(root.get_right())

        return count + 1
    
    # **************************************************************************
    # Wrapper function to get the sum of the data in the BST.
    #
    # param: none
    #
    # The function returns -1 if the BST is empty. Otherwise, the function
    # returns the average of the data in the BST.
    # ************************************************************************** 
    def find_sum(self) -> int:
        if self.__root == None:
            return 0

        #Gets the sum of the data and number of nodes in the BST. 
        return self.__find_sum_recursive(self.__root)
    
    # **************************************************************************
    # Recursive function to get the sum of the data in the BST.
    #
    # param: none
    #
    # The function returns the sum of the data in the BST and the number of
    # nodes.
    # ************************************************************************** 
    def __find_sum_recursive(self, root: Node) -> int:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0

        sum, temp = root.get_data()
        
        sum += self.__find_sum_recursive(root.get_left())
        sum += self.__find_sum_recursive(root.get_right())

        return sum
 
    # **************************************************************************
    # Wrapper function to get the average of the data in the BST.
    #
    # param: none
    #
    # The function returns -1 if the BST is empty. Otherwise, the function
    # returns the average of the data in the BST.
    # ************************************************************************** 
    def find_average(self) -> float:
        if self.__root == None:
            return -1

        #Gets the sum of the data and number of nodes in the BST. 
        sum, count = self.__find_average_recursive(self.__root)

        avg = sum / count   #Computes the average

        return avg

    # **************************************************************************
    # Recursive function to determine average of the data in the BST.
    #
    # param: none
    #
    # The function returns the sum of the data in the BST and the number of
    # nodes.
    # ************************************************************************** 
    def __find_average_recursive(self, root: Node) -> Tuple[int, int]:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0, 0
        
        sum, temp = root.get_data()
        count = 1

        #Traverses the left subtree.        
        temp_sum, temp_count = self.__find_average_recursive(root.get_left())

        sum += temp_sum       #Adds the sum of the data in the left subtree.
        count += temp_count   #Adds the number of nodes in the left subtree.

        #Traverses the right subtree.
        temp_sum, temp_count = self.__find_average_recursive(root.get_right())

        sum += temp_sum       #Adds the sum of the data in the right subtree.
        count += temp_count   #Adds the number of nodes in the right subtree.

        return sum, count

    # **************************************************************************
    # Wrapper function to retrieve a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be retrieved
    #
    # The function returns -1 if the BST is empty, 0 if the data item cannot
    # be found, or 1 if the data item was found.
    # ************************************************************************** 
    def retrieve(self, key: int) -> int:

        #Raises a value error if key is less than 15.
        if key < 15:
            raise ValueError

        #Returns -1 to the calling routine if the BST is empty.
        if self.__root == None:
            return -1 

        return self.__retrieve_recursive(self.__root, key)

    # **************************************************************************
    # Recursive function to remove a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be removed.
    #
    # The function returns 0 if the data item cannot be found. Otherwise, the 
    # function returns 1 if the data item was found.
    # ************************************************************************** 
    def __retrieve_recursive(self, root: Node, key: int) -> int:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0
        
        #If the current node's data matches the key...
        if root == key:
            print(f"\n{root}")
            return 1
 
        #Traverses the left subtree if the key is less than the current node's
        #data.
        if key < root:
            result = self.__retrieve_recursive(root.get_left(), key)

        #Traverses the right subtree if the key is greater than or equal to 
        #the current node's data.
        else:
            result = self.__retrieve_recursive(root.get_right(), key)
                
        return result

    # **************************************************************************
    # Wrapper function to remove a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be removed.
    #
    # The function returns -1 if the BST is empty, 0 if the data item cannot
    # be found, or 1 if the data item was found and removed.
    # ************************************************************************** 
    def remove(self, key: int) -> int:
        #Raises a value error if key is less than 15.
        if key < 15:
            raise ValueError

        #Returns -1 to the calling routine if the BST is empty.
        if self.__root == None:
            return -1

        #Removes the root if its data matches the key and it is the node in
        #the BST.        
        if self.__root == key:
            if not self.__root.has_left() and not self.__root.has_right():
                self.__root = None
 
        result, self.__root = self.__remove_recursive(self.__root, key)

        return result

    # **************************************************************************
    # Recursive function to remove a data item from the BST.
    #
    # key is passed the value corresponding to the data item to be removed.
    #
    # The function returns 0 if the data item cannot be found, or 1 if the data 
    # item was found and removed.
    # ************************************************************************** 
    def __remove_recursive(self, root: Node, key: int) -> Tuple[int, Node]:
        #Stops the recursive downward traversal down the current path of the 
        #tree and returns 0 to the calling routine if root is None.
        if root == None:
            return 0, root
        
        new_node = None
        coin_amount = 0
        turn = 0

        #If the current node's data matches the key...
        if root == key:

            #If the current node has a left child but not a right child...
            if root.has_left() and not root.has_right():

                #Saves the current node's left child reference.
                new_node = root.get_left()

            #If the current node has a left child but not a right child...
            elif not root.has_left() and root.has_right():

                #Saves the current node's right child reference.
                new_node = root.get_right()

            #If the current node has a left child and a right child...
            elif root.has_left() and root.has_right():


                #If the current node's right child does not have a left child...
                if not root.get_right().has_left():

                    #Replace the current node's data with its right child's
                    #data and assign the current node's right child reference
                    #to reference its right child's right child.
                    coin_amount, turn = root.get_right().get_data()
                    root.update_data(coin_amount, turn)
                    root.set_right(root.get_right().get_right())

                #Otherwise...
                else:
                    coin_amount, turn, temp = self.__remove_io_successor(root.get_right())
                    root.update_data(coin_amount, turn)

                new_node = root

            return 1, new_node
             
        result = 0
 
        #Traverses the left subtree if the key is less than the current node's
        #data.
        if key < root:
            result, new_node = self.__remove_recursive(root.get_left(), key)
            root.set_left(new_node)

        #Traverses the right subtree if the key is greater than or equal to 
        #the current node's data.
        else:
            result, new_node = self.__remove_recursive(root.get_right(), key)
            root.set_right(new_node)
                
        return result, root

    # **************************************************************************
    # Recursive function to remove and return the inorder successor's data.
    #
    # root is passed an object reference to the node being traversed.
    #
    # The function returns 0 if the data item cannot be found, or 1 if the data 
    # item was found and removed.
    # ************************************************************************** 
    def __remove_io_successor(self, root: Node) -> Tuple[int, int, Node]:

        if root == None:
            return 0, 0, root

        #If the current node does not have a left child...
        if not root.has_left():

            #Saves the current node's data and the reference to its right child.
            coin_amount, turn = root.get_data()
            right_child = root.get_right()

            root.display()

            #Return the current node's data and a reference to its right
            #child.
            return coin_amount, turn, right_child

        #Traverses the left subtree.
        coin_amount, turn, new_left = self.__remove_io_successor(root.get_left())

        #Sets the current node's left child reference to new_left.
        root.set_left(new_left)

        return coin_amount, turn, root



    





    
