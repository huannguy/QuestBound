import tree
import pytest

# TESTING THE NODE CLASS'S METHODS

#Tests the default constructor for the Node class.
def test_Node_object_Creation_Success():

    #Tests if a ValueError exception was raised if the coin
    #amount passed in is less than 15. 
    with pytest.raises(ValueError):
        object = tree.Node(10, 1)

    #Tests if a ValueError exception was raised if the turn
    #number passed in is less than 1.
    with pytest.raises(ValueError):
        object = tree.Node(15, 0)

    object = tree.Node(15, 1)

    assert object._Node__coins_earned == 15
    assert object._Node__turn == 1
    assert object._Node__left == None
    assert object._Node__right == None

#Tests the overloaded < operator for the Node class.
def test__lt__():
    object = tree.Node(15, 1)

    result = object < 20 
    assert result == True

    result = object < 15 
    assert result == False

#Tests the overloaded > operator for the Node class.
def test__gt__():
    object = tree.Node(15, 1)

    result = object > 10 
    assert result == True

    result = object > 15 
    assert result == False

#Tests the overloaded == operator for the Node class.
def test__eq__():
    object = tree.Node(15, 1)

    result = object == 15 
    assert result == True

    result = object == 20
    assert result == False


def test_update_data():  
    object = tree.Node(15, 1)

    new_coin_amount = 20
    new_turn_num = 2

    #Tests if the update_data function is correctly 
    #updating the data.
    object.update_data(new_coin_amount, new_turn_num)
    assert object._Node__coins_earned == new_coin_amount
    assert object._Node__turn == new_turn_num

    #Tests if a ValueError exception was raised if the coin
    #amount passed in is less than 15. 
    with pytest.raises(ValueError):
        object = tree.Node(10, 1)

    #Tests if a ValueError exception was raised if the turn
    #number passed in is less than 1.
    with pytest.raises(ValueError):
        object = tree.Node(15, 0)

def test_has_left(): 
    #Tests if the has_left() function returns
    #False if the node does not have a left child.
    object = tree.Node(15, 1)
    assert object.has_left() == False

    #Tests if the has_left() function returns
    #True if the node has a left child.
    new_node = tree.Node(15, 1)
    object._Node__left = new_node
    assert object.has_left() == True

def test_has_right(): 
    #Tests if the has_right() function returns
    #False if the node does not have a right child.
    object = tree.Node(15, 1)
    assert object.has_right() == False

    #Tests if the has_right() function returns
    #True if the node has a right child.
    new_node = tree.Node(15, 1)
    object._Node__right = new_node
    assert object.has_right() == True

def test_set_left(): 
    object = tree.Node(15, 1)
    new_node = tree.Node(20, 2)

    #Tests if the set_left() function is correctly
    #setting the node's left child reference to
    #reference the new node.
    object.set_left(new_node)
    assert object._Node__left == new_node

def test_set_right(): 
    object = tree.Node(15, 1)
    new_node = tree.Node(20, 2)

    #Tests if the set_right() function is correctly
    #setting the node's right child reference to
    #reference the new node.
    object.set_right(new_node)
    assert object._Node__right == new_node

def test_get_left(): 
    object = tree.Node(15, 1)
    new_node = tree.Node(20, 2)

    #Tests if the get_left() function is returning
    #the node's left child reference.
    object.set_left(new_node)
    assert object.get_left() == new_node

def test_get_right(): 
    object = tree.Node(15, 1)
    new_node = tree.Node(20, 2)
 
    #Tests if the get_right() function is returning
    #the node's right child reference.
    object.set_right(new_node)
    assert object.get_right() == new_node

def test_get_data(): 
    object = tree.Node(15, 1)

    coin_amount, turn = object.get_data()

    #Test if the data being returned matches what is in
    #the node.
    assert coin_amount == object._Node__coins_earned
    assert turn == object._Node__turn

# TESTING THE NODE CLASS'S METHODS

@pytest.fixture
def setup():
    return tree.Tree()

def test_Tree_object_Creation_Success(setup):
    assert setup._Tree__root == None

def test_insert(setup):

    #Tests if a ValueError exception was raised if the coin
    #amount passed in is less than 15
    with pytest.raises(ValueError):
        setup.insert(10, 1)

    #Tests if a ValueError exception was raised if the turn
    #number passed in is less than 1.
    with pytest.raises(ValueError):
        setup.insert(15, 0)

    assert setup.insert(15, 1) == 1

def test_display(setup):

    #Tests if the display() function returns 0 if
    #the tree is empty.
    setup._Tree__root = None
    assert setup.display() == 0

    #Tests if the display() function returns 1 if
    #one data item was displayed.
    setup.insert(15, 1) 
    assert setup.display() == 1

    #Tests if the display() function returns 2 if
    #two data items were displayed.
    setup.insert(20, 2) 
    assert setup.display() == 2

def test_find_sum(setup): 

    #Tests if the find_sum() function returns 0 if
    #the tree is empty.
    setup._Tree__root = None
    assert setup.find_sum() == 0

    #Tests if the find_sum() function returns the
    #correct sum of the reward amounts in the
    #tree.
    setup.insert(15, 3) 
    setup.insert(20, 6) 
    assert setup.find_sum() == 35

    setup.insert(26, 8) 
    setup.insert(17, 13) 

    assert setup.find_sum() == 78

def test_find_average(setup): 

    #Tests if the find_average() function returns -1 if
    #the tree is empty.
    setup._Tree__root = None
    assert setup.find_average() == -1

    #Tests if the find_average() function returns the
    #correct average of the reward amounts in the
    #tree.
    setup.insert(15, 3) 
    setup.insert(20, 6) 

    assert setup.find_average() == 17.5

    setup.insert(26, 8) 
    setup.insert(17, 13) 

    assert setup.find_average() == 19.5

def test_retrieve(setup): 

    #Tests if a ValueError exception was raised if the coin
    #amount passed in less a negative number.
    with pytest.raises(ValueError):
        setup.retrieve(-5)

    #Tests if the retrieve() function returns -1 if
    #the tree is empty.
    setup._Tree__root = None
    assert setup.retrieve(15) == -1

    #Builds a BST.
    setup.insert(15, 3) 
    setup.insert(20, 6) 
    setup.insert(22, 8) 
    setup.insert(28, 11) 


    #Tests if the retrieve() function returns 0 if the
    #specified entry could not be found or 1 if the
    #specified entry was found.
    assert setup.retrieve(15) == 1
    assert setup.retrieve(20) == 1
    assert setup.retrieve(22) == 1
    assert setup.retrieve(28) == 1
    assert setup.retrieve(21) == 0

def test_remove(setup): 

    #Tests if a ValueError exception was raised if the coin
    #amount passed in less a negative number.
    with pytest.raises(ValueError):
        setup.remove(-5)


    #Tests if the retrieve() function returns -1 if
    #the tree is empty.
    setup._Tree__root = None
    assert setup.remove(15) == -1

    #Builds a BST.
    setup.insert(25, 3) 
    setup.insert(20, 6) 
    setup.insert(22, 8) 
    setup.insert(28, 11) 

    #Tests if the remove() function returns 0 if the
    #specified entry could not be found or 1 if the
    #specified entry was found.
    assert setup.remove(25) == 1
    assert setup.remove(25) == 0

def test_remove_io_successor(setup): 
    setup._Tree__root = None

    coin_amount = 0
    turn = 0
    root = None

    #Tests if the remove_io_successor() function returns 0, 0, and None
    #if the tree is empty.
    coin_amount, turn, root = setup._Tree__remove_io_successor(root)

    assert coin_amount == 0 and turn == 0 and root == None

    #Builds a tree.
    setup.insert(25, 3) 
    setup.insert(20, 6) 
    setup.insert(22, 7) 
    setup.insert(28, 11) 
    setup.insert(26, 14) 

    coin_amount, turn, root = setup._Tree__remove_io_successor(setup._Tree__root._Node__right)

    setup._Tree__root = root
    setup._Tree__root.update_data(coin_amount, turn)


    #Tests if the remove_io_successor() function is returning the inorder successor's data.
    assert coin_amount == 26 and turn == 14 
    assert setup._Tree__root._Node__coins_earned == coin_amount and setup._Tree__root._Node__turn == turn
