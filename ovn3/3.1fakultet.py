def fakultet(n):
    '''Ta ett positivt heltal n eller 0 som input och returnera fakulteten av n, dvs
    n! = n*(n-1)(n-2)...2*1'''
    if type(n) != int:
        return
    if 0<=n:
        if 0 <= n < 2:
            return 1
        else:
            return n * fakultet(n-1)
    else:
        return
'''Koden för fakultetsfunktionen ovan är uppenbarligen densamma som fakulteten av n
för fallen n=1 och n = 0. Induktionsbevis ger att jag vill bevisa likheten
(n+1)! = (n+1) * fakultet(n). Induktionsantagandet säger oss att fakultet(n) = n!.
Lös ut n+1 från VL i (n+1)! = (n+1) * fakultet(n) och en ser då med hjälp av
induktionsantagandet att likheten stämmer. Algoritmen till fakultetsfunktionen
returnerar None om n < 0'''

assert fakultet(5) == 5*4*3*2
assert fakultet(0) == 1
assert fakultet(4) == 4*3*2
assert fakultet([2, 3, 27378]) == None
assert fakultet('hh') == None
assert fakultet(1.234) == None
assert fakultet(True) == None
assert fakultet(-34) == None
print('fungerar')
