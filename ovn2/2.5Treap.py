import random

class Nod:
    def __init__(self, int_value, string):
        self.int_value = int_value
        self.string = string
        self.priority = random.uniform(0,1)
        self.left = None
        self.right = None
        self.foralder = None


class Treap:
    def __init__(self):
        self.rot = None
        self.antal = 0

    def rotation_right(self,nuvarande_nod):
        a = nuvarande_nod
        b = a.left
        a.left = b.right
        b.right = a
        return b

    def rotation_left(self,nuvarande_nod):
        a = nuvarande_nod
        b = a.right
        a.right = b.left
        b.left = a
        return b


    def add(self, string):
        self.antal += 1
        self.string_converter = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,'f':6,'g':7, 'h':8, 'i':9,'j':10, 'k':11, 'l':12, 'm':13, 'n':14,'o':15,'p':16, 'q':17,'r':18, 's':19, 't':20, 'u':21,'v':22,'w':23, 'x':24, 'y':25, 'z':26}
        self.rot = self._add_rekursion(self.rot, self.string_converter[string[0]], string)


    def _add_rekursion(self, nuvarande_nod, int_value, string):

        if type(string) != str:
            self.antal -= 1
            return
        if nuvarande_nod == None:
            nuvarande_nod = Nod(int_value, string)
            return nuvarande_nod
        if int_value < nuvarande_nod.int_value:
            nuvarande_nod.left = self._add_rekursion(nuvarande_nod.left, int_value, string)
            if nuvarande_nod.left.priority < nuvarande_nod.priority:
                nuvarande_nod = self.rotation_right(nuvarande_nod)
        elif int_value >= nuvarande_nod.int_value:
            nuvarande_nod.right = self._add_rekursion(nuvarande_nod.right, int_value, string)
            if nuvarande_nod.right.priority < nuvarande_nod.priority:
                nuvarande_nod = self.rotation_left(nuvarande_nod)
        return nuvarande_nod
        '''Värstafalls komplexiteten O(n) när trädet blir som en länkad lista'''

    def sortera(self, rot):
        v = []
        if rot:
            v = self.sortera(rot.left)
            v.append(rot.string)
            v = v + self.sortera(rot.right)
        return v

    def size(self):
        return self.antal


    def clear(self):
        # Värstafalls komplexitet O(n), samma som den för garbage collectorn
        self.rot = None
        self.antal = 0
        return



def test():
    B = Treap()
    number_of_elements_test = 0
    for i in ['qwa','qwsd','frev','kerm','vre', 'ed','red', 'de']:
        number_of_elements_test += 1
        B.add(i)
    if B.rot:
        if B.rot.left:
            assert B.rot.left.priority > B.rot.priority
        if B.rot.right:
            assert B.rot.right.priority > B.rot.priority
    assert B.size() == number_of_elements_test
    print(B.sortera(B.rot))
    B.clear()
    assert B.size() == 0
    assert B.rot == None
    print('Working!')
test()
