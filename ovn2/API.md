## Unbalanced binary search tree

An unbalanced binary search tree is a container of data. Sort of like a linked list but each added string
(in our case) goes alphabetically to the left if the first letter of the added string goes before the
first letter of the string in the checked node. Opposite if the first letter of the added string goes
after the first letter of the string in the checked node. If the first letters are the same for the
string in the current node and the string you want to add then you check for the second letter, if those
are the same you check the third and so on...

The code for the binary tree implemented here is in the same repository as this file. The binary tree
created can add new elements, remove all current nodes or elements as well as determine the number of
elements in the tree.

Below is a description of what every function in a program for this binary search tree does:

### Class Nod:

This is a class that is containing the string that has been added. It also contains three pointers
pointing on the node's parent as well as its left and right child.
Example code from VGlabb2.py:

    class Nod:
        def __init__(self,string=None):
            self.string=string
            self.left=None
            self.right=None
            self.foralder=None



Class Binart_soktrad:
This class should contain the value of the root, the number of elements in the tree and a counter for the letter of a string you are currently looking at, for example if it is the 5:th letter you are comparing then self.num will be equal to 5.
Example code from VGlabb2.py:

    class Binart_soktrad:
        def __init__(self):
            self.rot = None
            self.num = 0
            self.antal = 0



Function add():
Worst case complexity O(b*n), n is the number of elements in the tree and b is the number of letters in the string you want to add. This happens when it is calling add_rekursion which has worst case
complexity O(b*n) (see below). This function should go within the Binart_soktrad class and contain a call to the
function add.rekursion() which is described below. But what this function does is to add elements to the tree/list.
Example code from VGlabb2.py:

    def add(self,string):
        if self.rot==None: # I the tree is empty add the first string here
            self.antal += 1
            self.rot=Nod(string)
        else:
            self.add_rekursion(string,self.rot)
            return


### Function add_rekursion():

Worst case complexity O(b*n). To calculate the worst case time complexity I must consider the worst case
which is as follows: If the string being added has a last letter (we call it letter number b) that goes before alphabetically than
all the other b:th letters of the strings in the tree then
the function add_rekursion will be called n (the number of elements in the tree) times. string_converter will have time complexity O(1) within each call, but will always be called when add_rekursion is called. string_converter will at the worst case be called for every letter in the string and the number of letters in the string that is being added is b. add_rekursion
should go within the Binart_soktrad class and should only be called from add().
It will take the input string and add it to the place it is supposed to be in the tree. If a node in the
tree already contains a string then the pointers, we call them left or right, of the object will be
pointed left or right or create a new node if the pointer (left or right) is pointing on None. If the node
the pointer is pointing on is already taken then the pointer will be updated, add_rekursion will be called
again and the same procedure goes on until an empty node (an object with value none) has been found.
Within add_rekursion a function string_converter will be called to convert the strings to integers so each
letter in the string can be represented as integers and from there be compared in value with the current
nodes in the tree.

Example code:

    def add_rekursion(self,string,nuvarande_nod):
        if (nuvarande_nod.string in string or string in nuvarande_nod.string) and nuvarande_nod.string[0] == string[0]: #If the beginning letters of the string in the current node you are looking at contains the same letters as the string you want to add or if the beginning letters of the string you want to add contains the same letters as the letters in the string in the node you are looking at, then there is no way to know where to place the string you want to add.
            self.num = 0
            return None
        string_varde = self.string_converter(string)
        nu_str_varde = self.string_converter(nuvarande_nod.string)
        if string_varde < nu_str_varde:  
            self.num = 0
            if nuvarande_nod.left == None: # If the left child of the current node is None and the letter you are looking at in the string you want to add goes before the corresponding letter in the current node. Then you want to make the string you want to add to the current node's left child.         
                self.antal += 1
                nuvarande_nod.left=Nod(string)
                nuvarande_nod.left.foralder=nuvarande_nod # set foralder
                return
            else:  # If the left child of the current node is not None and the letter you are looking at in the string you want to add goes before the the corresponding letter in the current node. Then you want to move to the left child of the current node and call add_rekursion until there is an available node with the value None.
                self.add_rekursion(string,nuvarande_nod.left)
                return
        elif string_varde > nu_str_varde:
            self.num = 0
            if nuvarande_nod.right==None: # If the right child of the current node is None and the letter you are looking at in the string you want to add goes after the corresponding letter in the current node. Then you want to make the string you want to add to the current node's right child.
                self.antal += 1
                nuvarande_nod.right=Nod(string)
                nuvarande_nod.right.foralder=nuvarande_nod # set foralder
                return
            else:  # If the right child of the current node is not None and the letter you are looking at in the string you want to add goes after the corresponding letter in the current node. Then you want to move to the right child of the current node and call add_rekursion until there is an available node with the value None.
                self.add_rekursion(string,nuvarande_nod.right)
                return
        else: # In all other cases check for the next letter of the string in the current node and the corresponding letter in the string you want to add, call add_rekursion.
            self.num += 1
            self.add_rekursion(string,self.rot)
            return



### Function string_converter:

Worst case complexity O(1), where b is the number of letters for the added string.
This function should go within the Binart_soktrad class and should convert the
first letter of the string
input to an integer with letter 'a' being an integer with value 1 and z being
integer with value y<, 26
for example.

Example code:

    def string_converter(self, string):

        if type(string) == str and string[self.num] in 'aA':
            return 1
        elif type(string) == str and string[self.num] in 'bB':
            return 2
        elif type(string) == str and string[self.num] in 'cC':
            return 3
        elif type(string) == str and string[self.num] in 'dD':
            return 4
        elif type(string) == str and string[self.num] in 'eE':
            return 5
        elif type(string) == str and string[self.num] in 'fF':
            return 6
        elif type(string) == str and string[self.num] in 'gG':
            return 7
        elif type(string) == str and string[self.num] in 'hH':
            return 8
        elif type(string) == str and string[self.num] in 'iI':
            return 9
        elif type(string) == str and string[self.num] in 'jJ':
            return 10
        elif type(string) == str and string[self.num] in 'kK':
            return 11
        elif type(string) == str and string[self.num] in 'lL':
            return 12
        elif type(string) == str and string[self.num] in 'mM':
            return 13
        elif type(string) == str and string[self.num] in 'nN':
            return 14
        elif type(string) == str and string[self.num] in 'oO':
            return 15
        elif type(string) == str and string[self.num] in 'pP':
            return 16
        elif type(string) == str and string[self.num] in 'qQ':
            return 17
        elif type(string) == str and string[self.num] in 'rR':
            return 18
        elif type(string) == str and string[self.num] in 'sS':
            return 19
        elif type(string) == str and string[self.num] in 'tT':
            return 20
        elif type(string) == str and string[self.num] in 'uU':
            return 21
        elif type(string) == str and string[self.num] in 'vV':
            return 22
        elif type(string) == str and string[self.num] in 'wW':
            return 23
        elif type(string) == str and string[self.num] in 'xX':
            return 24
        elif type(string) == str and string[self.num] in 'yY':
            return 25
        elif type(string) == str and string[self.num] in 'zZ':
            return 26
        else:
            return



### Function clear():

Worst case complexity O(n), the same as the one for the garbage collector.
This function should go within the Binart_soktrad class and should remove all elements from the tree. It
should do this by pointing the root instance variable on None. The instance variable containing the
integer of the number of elements in the tree should be set to 0.
Example code:

    def clear(self):
        self.rot = None
        self.antal = 0
        return




### Function test():

This function should test the methods of the class of the binary tree (Binart_soktrad).

Example code:

    def test():
        B = Binart_soktrad()
        n = 13
        number_of_elements_test = 0
        for i in ['qwa','qwsd','frev','kerm','vre', 'ed','vred', 'de']:
            number_of_elements_test += 1
            B.add(i)
        number_of_elements_test -= 1    # 'vre' already exist in the tree when 'vred' is to be added, therefore it is impossible to say where 'vred' is to be placed so 'vred' doesn't exist in the tree and number_of_elements_test is subtracted by 1
        assert B.size() == number_of_elements_test
        assert B.rot.right.string == 'qwsd'
        B.clear()
        assert B.size() == 0
        assert B.rot == None
        print('Working!')
