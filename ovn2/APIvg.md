### class public Nod
    private in_value #int representation of input string
    private string
    private priority
    private left
    private right
    private foralder

### class public Treap
    private rot
    private antal


#Rotate tree so that the priority objects with lower priority values goes higher up in the tree. Time complexity O(1)

public rotation_right() nuvarande_nod


#Same as above but rotate in the other direction. Time complexity O(1)

public rotation_left() nuvarande_nod

#Add string to the tree. Worst time complexity O(n) same for function _add_recursion below.

public add() string


#Recursive function, should only be called from add(), contains calls to rotation_right and rotation_left. Returns the full tree with the added string. 

private _add_recursion() nuvarande_nod, int_value, string #Worst case time complexity O(n). Avarage is O(log(n)).


#Sorts the strings in the list alphabeticaly. Time complexity O(n)

public sortera() rot(pointer)

#Returns the number of strings in the tree. O(1)

public size()

#Removes all elements from the tree. Time complexity O(n), same as for the garbage collector

public clear()