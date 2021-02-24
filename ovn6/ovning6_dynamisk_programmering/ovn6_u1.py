
def p(n):
    '''returnerar den maximala inkomsten'''
    if type(n) != int:
        return
    if n == 0:
        return 0
    list = []
    for i in range(1, n+1):
        list.append(h[i] + p(n-i))
    return max(list)
"""Algoritmen ovan kommer att ha tidskomplexiteten Θ(a^n). En kan lätt se
att algoritmen måste vara Θ(a^n), p(n+1) kommer kräva ungefär dubbelt så många steg som p(n). I
fallet p(n+1) så kommer i steget när en funktion p(n) ska returnera ungefärsamma funktionsanrop
göras igen innan p(n+1) returnerar dvs ungefär dubbelt så många steg som p(n)."""






def p_memorization(n, store = {}):
    '''returnerar den maximala inkomsten'''
    if type(n) != int:
        return
    if n == 0:
        return 0
    if n in store:
        return store[n]
    list = []
    for i in range(1, n+1):
        list.append(h[i] + p_memorization(n-i))
    store[n] = max(list)
    return store[n]
"""Algoritmen använder memorisering och cachar delresultat i en
dictionary. Anledningen till varför
tidskomplexiteten blir Θ(n^2) är för att jag måste beräkna max värdet av k
st uttryck för att beräkna p(k),
där k = 1,2,...,n (alla p(m), där m < k, har redan beräknats och är redan
kända). Detta går att uttrycka
som en summa från 1 till n, vilket är ett uttryck av n kvadrat och därmed
är algoritmen ovan Θ(n^2)"""


h = [0,2,5,6,9,0]
def test():
    n = 5
    for i in range(1,n+1):
        assert p_memorization(i) == p(i)
    assert p(5) == 12 #Samma som jag räknade ut för hand
    assert p(12.0) == None
    assert p_memorization('weded') == None
    print('fungerar!')

test()
