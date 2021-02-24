# -*- coding: <utf-8> -*-

class _Listelement:
    def __init__(self, varde_input=None):
        self.varde_input = varde_input
        self.next = None

class Linkedlist:
    def __init__(self):
        self.__forsta_pekare = None
        self.__antal = 0
        self.__last = None

# Lägger till data i början av en lista
    def addFirst(self, nytt_varde):
#Värstafallstiden O(1)
        self.__antal += 1
        ny_pekare = _Listelement(nytt_varde)
        if self.__forsta_pekare == None:
            self.__forsta_pekare = ny_pekare
            self.__last = ny_pekare
            return
        store = self.__forsta_pekare
        self.__forsta_pekare = ny_pekare
        ny_pekare.next = store
        ny_pekare = None


# Lägger till data i slutet av listan
    def addlast(self, nytt_varde):
#Värstafallstiden O(n)
        self.__antal += 1
        ny_pekare = _Listelement(nytt_varde)
        if self.__forsta_pekare == None:
            self.__forsta_pekare = ny_pekare
            return
        else:
            sist = self.__forsta_pekare
            while sist.next:
                sist = sist.next
            sist.next = ny_pekare
        self.__last = ny_pekare
        return


# Hämtar första elementet från listan
    def getFirst(self):
#Värstafallstiden O(1)
        if self.__forsta_pekare == None:
            return
        else:
            return self.__forsta_pekare.varde_input

# Hämtar sista elementet från listan
    def getlast(self):
#Värstafallstiden O(n), n är __antalet element
        if self.__forsta_pekare == None:
            return
        else:
            sist = self.__forsta_pekare
            while sist.next:
                sist = sist.next
            return sist.varde_input


# Jag delar upp i två fall, get() returnerar elementet på den specifierade positionen om indexet existerar i listan annars returneras None
    def get(self, index):
#Värstafallstiden O(n), n är __antalet element
        if self.__forsta_pekare == None:
            return
        counter = 0
        help_pointer = self.__forsta_pekare
        while help_pointer:
            help_pointer = help_pointer.next
            counter += 1
        if 1 <= index <= counter and type(index) == int:
            counter = 1
            help_pointer = self.__forsta_pekare
            while index != counter:
                help_pointer = help_pointer.next
                counter += 1
            return help_pointer.varde_input
        else:
            return


    def removeFirst(self):
#Värstafallstiden O(1)
        if self.__forsta_pekare == None:
            return
        self.__antal -= 1
        forst = self.__forsta_pekare.varde_input
        self.__forsta_pekare = self.__forsta_pekare.next
        return forst


    def clear(self):
#Värstafallstiden O(n)
        self.__antal = 0
        self.__forsta_pekare = None
        return


# Återanvänd kod från get()
    def size(self):
#Värstafallstiden O(n), n är __antalet element
        if self.__forsta_pekare == None:
            return 0
        counter = 0
        help_pointer = self.__forsta_pekare
        while help_pointer:
            help_pointer = help_pointer.next
            counter += 1
        return counter


# Skriv ut länkad lista
    def string(self):
#Värstafallstiden O(n), n är __antalet element
        counter = 0
        utskrift = ''
        skriv_ut = self.__forsta_pekare
        if skriv_ut == None:
            return '[]'
        while skriv_ut != None:
            utskrift += str(skriv_ut.varde_input) + ", "
            skriv_ut = skriv_ut.next
            counter += 1
        assert counter == self.__antal
        utskrift = utskrift[:-2]
        return  '['+ utskrift  + ']'

    def healthy(self):
        assert self.size() == self.__antal

        if self.__antal == 0:
            self.getlast() == None
            self.getFirst() == None

        else:
            assert self.getFirst() != None
            assert self.getlast() != None
            assert self.getlast() == self.get(self.__antal)
            assert self.get(self.__antal + 1) == None # Detta visar att getlast.next är None




import random

def Test():
    n = 4
    k = 7
    x = random.randint(1,n-1)
    l = Linkedlist()
    assert l.size() == 0
    assert l.string() == '[]'
    l.healthy()
    for i in range(1,n):
        l.addlast(i)
    assert l.size() == n - 1
    assert l.getFirst() == 1
    assert l.getFirst() == l.get(1)
    assert l.getlast() == n-1
    assert l.getlast() == l.get(n-1)
    assert l.get(n+12) == None
    assert l.get(x) == x
    assert l.removeFirst() == 1
    assert l.getFirst() == 2
    l.addFirst('Hello')
    assert l.getFirst() == 'Hello'
    l.healthy()
    l.clear()
    l.healthy()
    x = random.randint(1,k-1)
    assert l.size() == 0
    assert l.string() == '[]'
    for i in range(1,k):
        l.addlast(i)
    assert l.size() == k-1
    assert l.getFirst() == 1
    assert l.getFirst() == l.get(1)
    assert l.getlast() == k-1
    assert l.get(k-1) == l.getlast()
    assert l.get(k+90) == None
    assert l.get(x) == x
    assert l.removeFirst() == 1
    assert l.getFirst() == 2
    l.addFirst('njiijnhb')
    assert l.getFirst() == 'njiijnhb'
    l.healthy()

    print('Fungerar!')

Test()
