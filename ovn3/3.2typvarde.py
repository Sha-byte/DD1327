'''Pythons inbyggda sort använder en effektiv variant av mergesort.
Mergesort har värsta tidskomplexiteten O(n*log(n))'''

def typvarde(vektor):
    n = len(vektor) #O(n)
    vektor.sort() #O(n*log(n))
    max = 1
    typ = vektor[0]
    nuvarande = 1

    for i in range(1, n): #O(n)
        if (vektor[i] == vektor[i - 1]):
            nuvarande += 1

        else :
            if (nuvarande > max):
                max = nuvarande
                typ = vektor[i - 1]

            nuvarande = 1

    # Om sista elementet är det vanligaste
    if (nuvarande > max):

        max = nuvarande
        typ = vektor[n - 1]

    return typ

assert typvarde([1, 6, 6, 5, 2, 1, 6, 3, 1, 2, 6, 1]) == 1
assert typvarde([ 33, 2, 87, 4, 9, 87, 2, 87, 4]) == 87
print('working')

'''Tiden i algoritmen ovan kan uttryckas som k*n*log(n) + s*n, för
positiva konstanter k och s. k*n*log(n) + s*n = O(n*log(n))'''
