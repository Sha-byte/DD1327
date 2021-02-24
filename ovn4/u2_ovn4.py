def int_sort(v, k):
    '''Tar en lista v och ett heltal k som är större än alla element
    i listan som input. Därefter returneras den sorterade listan med element
    i stigande ordning'''
    n = len(v)
    temp = [0] * n
    count = [0] * k

    for i in range(0, n):
        count[v[i]] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    i = n - 1
    while 0 <= i:
        temp[count[v[i]] - 1] = v[i]
        count[v[i]] -= 1
        i -= 1

    for i in range(0, n):
        v[i] = temp[i]
    return v
'''Algoritmen ovan har värsta tidskomplexiteten O(n+k) om k är mindre än eller lika med n så blir tidskomplexiteten linjär dvs O(n).
Rent allmänt gäller att måste vara k måste tillhöra O(n).
För att detta ska vara möjligt måste det finnas flera av samma element i input listan v.
För att algotitmen ska bli så effektiv som möjligt sätts k rimligtvis till max(v) + 1.
k måste vara ett heltal större än det största elementet i listan för att algoritmen ovan ska fungera'''
def test():
    import random
    v = []
    w =[]
    n = 30
    r = 20
    for i in range(n):
        s = random.randint(1,r)
        v.append(s)
    w = v.copy()
    w.sort()
    k = max(v) + 1
    assert int_sort(v, k) == w

test()
