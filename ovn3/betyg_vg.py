
def typ_varde(v):
    '''Sätt in en lista med heltal som input i den här funktionen så
    kommer den returnera typvärdet, dvs det heltal som förekommer
    flest gånger i listan. Om flera heltal förekommer flest gånger,
    då kommer det minsta av de heltalen returneras'''
    if type(v) != list:
        return

    # Sätt in alla element i en dictionary
    dictionary = dict()
    for i in range(len(v)): #O(n)
        if v[i] in dictionary.keys():
            dictionary[v[i]] += 1
        else:
            dictionary[v[i]] = 1
    '''Ovan skapas en dictionary med variabelnamnet dictionary. dictionary innehåller
    värderna i input listan v som nycklar och de
    respektive värderna som korresponderar till nycklarna är antalet ggr listelementet av
    det värdet förekommer i input listan. Så om input listan t.ex är [3, 2, 3] då är
    dictionary[3] = 2 eftersom talet 3 förekommer 2 ggr i listan. Ovan har värstafallet O(n).'''
    # Maximala antalet ggr ett tal uppstår
    max = 0
    typ = -1
    for i in dictionary: #O(n)
        if max < dictionary[i]:
            typ = i
            max = dictionary[i]
            '''Jag undersöker alla key value pairs till dictionary. Om ett värde skulle
            förekomma fler gånger i en lista än något annat så tilldeles en variabel som
            kallas max antalet ggr värdet förekommer i listan, vilket en lätt kan få fram
            genom dictionary[v[k]]. List elementets värde vilket är nyckeln i dictionaryn
            sparas i en variabel som kallas typ. Alla nycklar och korresponderande värden
            till nycklarna undersöks på det här sättet, när for loopen avslutas kommer alltså
            typ innehålla värdet på det list element som förekommer flest gånger i input listan v.'''
        elif max == dictionary[i] and i < typ:
            typ = i
            max = dictionary[i]
            '''Om något list element vi kallar v[k] skulle förekomma lika många gånger som
            det list element som av de som hitills har undersökts har förekommit flest
            gånger som vi kallar v[m]. Då tilldelas typ v[k] endast om v[k] är mindre än
            v[m]'''
    return typ
'''Ovan har värstafallet O(n). Eftersom två for loopar efter varandra gör att värsta tidskomplexiteten blir linjär'''


def neg_first(v):
    '''Tar en lista v med floats eller integers som input och returnerar en ändrad lista
    med samma tal men så att de negativa talen är först'''
    i = 0
    for k in range(len(v)):
        ''' Invariant: dellistan v[0...i] innehåller alla de negativa talen i v från 0 till indexet k i ingen specifik ordning.'''
        if (v[k] < 0):
            v[i], v[k] = v[k], v[i] #Byter plats på v[i] och v[k]
            i += 1
    return v
'''I varje iteration av for loopen ovan så placeras ett list element i början av listan v
endast om det list elementet är mindre än noll. Detta görs endast med O(1) extra minne genom
att byta plats på elementet på indexet i och det undersökande indexet k endast om v[k] är
mindre än noll sedan måste i inkrementeras med ett för att nästa list element som  är mindre
än noll ska placeras på platsen v[i + 1] i listan. Varje enskilt element i listan v
undersöks på det sättet. Endast en for loop meför värsta tidskomplexiteten O(n)'''

def test_typ_varde():
    '''Testfunktion till typ_varde()'''
    v1 = [ 1, 0, -34, -34, 5, 2, 1, -34, 2, 1]
    v2 = [13, 52, -12, 13, 52, 13, 3, -12]
    v3 = [7, 3, -5, -6, 2, 4]
    assert typ_varde(v1) == -34
    assert typ_varde(v2) == 13
    assert typ_varde(v3) == -6

    print('fungerar')

def test_neg_first():
    '''Testfunktion till neg_first'''
    import random
    n = 23 #storleken
    a = -2.3
    b = 3.0
    v = []
    counter = 0

    for i in range(n):
        v.append(random.uniform(a, b))
        if v[i] < 0:
            counter += 1

    w = neg_first(v)
    for i in range(counter):
       assert w[i] < 0
    print('fungerar')
    '''counter räknar hur många list element som är mindre än noll. Alla counter första list
    element måste vara mindre än noll för att neg_first ska fungera'''


test_typ_varde()
test_neg_first()
