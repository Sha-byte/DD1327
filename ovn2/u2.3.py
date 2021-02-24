class Nod:
    def __init__(self,string=None):
        self.string=string
        self.left=None
        self.right=None
        self.foralder=None # pointer to foralder Nod in tree

class Binart_soktrad:
    def __init__(self):
        self.rot = None
        self.num = 0
        self.antal = 0

    def add(self,string):
#Värstafalls komplexitet O(n)
        if self.rot==None:
            self.antal += 1
            self.rot=Nod(string)
        else:
            self.add_rekursion(string,self.rot)
            return

    def add_rekursion(self,string,nuvarande_nod):
#Värstafalls komplexitet O(n)
        if (nuvarande_nod.string in string or string in nuvarande_nod.string) and nuvarande_nod.string[0] == string[0]:
            self.num = 0
            return None
        string_varde = self.string_converter(string)
        nu_str_varde = self.string_converter(nuvarande_nod.string)
        if string_varde < nu_str_varde:
            self.num = 0
            if nuvarande_nod.left == None:
                self.antal += 1
                nuvarande_nod.left=Nod(string)
                nuvarande_nod.left.foralder=nuvarande_nod # set foralder
                return
            else:
                self.add_rekursion(string,nuvarande_nod.left)
                return
        elif string_varde > nu_str_varde:
            self.num = 0
            if nuvarande_nod.right==None:
                self.antal += 1
                nuvarande_nod.right=Nod(string)
                nuvarande_nod.right.foralder=nuvarande_nod # set foralder
                return
            else:
                self.add_rekursion(string,nuvarande_nod.right)
                return
        else:
            self.num += 1
            self.add_rekursion(string,self.rot)
            return

    def sortera(self, rot):
        v = []
        if rot:
            v = self.sortera(rot.left)
            v.append(rot.string)
            v = v + self.sortera(rot.right)
        return v



    def size(self):
# Värstafalls komplexitet O(1)
        return self.antal


    def clear(self):
# Värstafalls komplexitet O(n), samma som den för garbage collectorn
        self.rot = None
        self.antal = 0
        return

    def string_converter(self, string):
# Värstafalls komplexitet O(b), b är antalet bokstäver i den tillagda strängen
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


def test():
    B = Binart_soktrad()
    n = 13
    number_of_elements_test = 0
    for i in ['qwa','qwsd','frev','kerm','vre', 'ed','vred', 'de']:
        number_of_elements_test += 1
        B.add(i)
    number_of_elements_test -= 1    # 'vre'finns redan i trädet när vred ska läggas till, därmed är det omöjligt att säga var vred ska placeras och vred måste minskas med ett
    assert B.size() == number_of_elements_test
    assert B.rot.right.string == 'qwsd'
    print(B.sortera(B.rot))
    B.clear()
    assert B.size() == 0
    assert B.rot == None
    print('Working!')
test()
