def neg_first(v):
    i = 0
    for k in range(len(v)):
        if (v[k] < 0):
            v[i], v[k] = v[k], v[i] #Byter plats på v[i] och v[k]
            i += 1
    return v


def test():
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

test()
