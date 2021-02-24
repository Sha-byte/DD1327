def sort_int(v):
    '''Tar en lista v innehållande heltal (får innehålla dubletter) som input och returnerar en lista
    som innehåller samma element men med talen sorterade i stigande ordning'''
    if type(v) != list:
        return

    w = []
    n = len(v)
    m = 0
    a = 0
    output = [0]*n
    # Sätt in alla element i en dictionary
    dictionary = dict()
    for i in range(n): #O(n)
        if v[i] in dictionary.keys():
            dictionary[v[i]] += 1
        else:
            dictionary[v[i]] = 1

    for i in dictionary:
        #'''O(k), w innehåller alla unika element i v'''
        w.append(i)

    merge(w)
    '''Anropar merge() som har tidskomplexiteten O(k*log(k))'''

    for k in w: #O(n)
        for i in range(dictionary[k]):
            output[m] = w[a]
            m += 1
        a += 1

    return output
    '''Totala tidskomplexiteten blir O(n) + O(k*log(k)) = O(n + k*log(k))'''

def merge(input_list):
    '''Tar en lista v innehållande heltal som input och returnerar en lista
    som innehåller samma element men med talen sorterade i stigande ordning'''
    if 1 < len(input_list):
        mid = len(input_list)//2
        v_list = input_list[:mid] # len(input_list) == 2^n. Anropas n ggr
        h_list = input_list[mid:]

        merge(v_list)
        merge(h_list)

        v_counter=0
        h_counter = 0
        counter=0
        while h_counter < len(h_list) and v_counter < len(v_list):
            if v_list[v_counter] <= h_list[h_counter]:
                input_list[counter]=v_list[v_counter]
                v_counter+=1
            else:
                input_list[counter]=h_list[h_counter]
                h_counter+=1
            counter+=1

        while v_counter < len(v_list):
            input_list[counter]=v_list[v_counter]
            v_counter+=1
            counter+=1

        while h_counter < len(h_list):
            input_list[counter]=h_list[h_counter]
            h_counter+=1
            counter+=1
        return

def test():
    '''testfunktion till sort_int()'''
    import random
    v = []
    n = 100
    for i in range(n):
        v.append(random.randint(-343,311))
    w = v.copy()
    v.sort()
    assert v == sort_int(w)
    assert sort_int('xewcd') == None
    print('fungerar!')

test()
