# -*- coding: <utf-8> -*-

import Ind_projekt as ind
import random
import numpy as np

def test():
    '''Testfunktion till alla funktioner i filen Ind_projekt.py'''
    r1 = random.randint(1,50)
    r2 = random.randint(1,50)
    r3 = random.randint(1,50)
    r4 = random.randint(1,50)
    r5 = random.randint(1,50)
    r6 = random.randint(1,50)
    r7 = random.randint(1,50)
    r8 = random.randint(1,50)
    r9 = random.randint(1,50)
    r10 = random.randint(1,10)
    r11 = random.randint(1,10)
    r12 = random.randint(1,10)
    r13 = random.randint(1,10)
    A1 = np.random.uniform(-10000.0,10000.0, size = (r1,r2))
    A2 = np.random.uniform(-10000.0,10000.0, size = (r1,r2))
    skalar = random.uniform(-10000.0,10000.0)
    A_scalar = np.random.uniform(-10000.0,10000.0, size = (r3,r4))
    A3 = np.random.uniform(-10000.0,10000.0, size = (r5,r6))
    A4 = np.random.uniform(-10000.0,10000.0, size = (r6,r7))
    A5 = np.random.uniform(-10000.0,10000.0, size = (r8,r9))
    A_det1 = np.random.uniform(-50.0,50.0, size = (r10,r10))
    A_det2 = np.random.uniform(-50.0,50.0, size = (r11,r11))
    A_invers1 = np.random.uniform(-50.0,50.0, size = (r12,r12))
    A_invers2 = np.random.uniform(-50.0,50.0, size = (r13,r13))

    assert ind.matrix_check([[5,4,1],[2,1],[1,5,3]]) == False
    assert ind.matrix_check('rkfm') == False
    assert ind.matrix_check([[-1.93, 0.34, 3],[12,-23.0928,-67],[23.43,-1.43234,-953628.1233],[-423.34, 9230, -5783.2903]]) == [4,3]

    a = ind.matrix_addition(A1,A2)
    b = np.add(A1,A2)
    for row in range(r1):
        for col in range(r2):
            assert b[row][col] - abs(b[row][col])*1.0e-10 <= a[row][col] <= b[row][col] + abs(b[row][col])*1.0e-10
    assert ind.matrix_addition([[-456,-23, 532],[-13,8,-34]],[[-23,7,4], [90,24,-86]]) == [[-479, -16, 536], [77, 32, -120]]


    c = np.array(A_scalar) * skalar
    d = ind.scalar(skalar, A_scalar)
    for row in range(r3):
        for col in range(r4):
            assert c[row][col] - abs(c[row][col])*1.0e-10 <= d[row][col] <= c[row][col] + abs(c[row][col])*1.0e-10
    assert ind.scalar(17,[[24,-76,32,75,-867,-9,-987,67,456,-345],[43,-5435,657,-868,979,-657,-346,-345,6457,-65]]) == [[408, -1292, 544, 1275, -14739, -153, -16779, 1139, 7752, -5865], [731, -92395, 11169, -14756, 16643, -11169, -5882, -5865, 109769, -1105]]


    e = np.dot(A3,A4)
    f = ind.matrix_multiplication(A3,A4)
    for row in range(r5):
        for col in range(r7):
            assert e[row][col] - abs(e[row][col])*1.0e-10 <= f[row][col] <= e[row][col] + abs(e[row][col])*1.0e-10
    assert ind.matrix_multiplication([[-2,63,32],[12,-23,0],[2,23,9],[14,54,11]],[[32,13,-1999,12],[-54,23,1,99],[9,67,-65,20]]) == [[-3178, 3567, 1981, 6853], [1626, -373, -24011, -2133], [-1097, 1158, -4560, 2481], [-2369, 2161, -28647, 5734]] #Stämmer överens med vad jag får vid beräkning för hand och matrismultiplikations miniräknare


    g = np.transpose(A5)
    h = ind.transponat(A5)
    for row in range(r9):
        for col in range(r8):
            assert g[row][col] - abs(g[row][col])*1.0e-10 <= h[row][col] <= g[row][col] + abs(g[row][col])*1.0e-10
    assert ind.transponat([[7,3],[4,10],[30,-54],[21,-9],[-32,0]]) == [[7, 4, 30, 21, -32], [3, 10, -54, -9, 0]]


    i = np.linalg.det(A_det1)
    j = ind.determinant(A_det1)
    assert i - abs(i)*1.0e-10 <= j <= i + abs(i)*1.0e-10

    k = np.linalg.det(A_det2)
    l = ind.determinant(A_det2)
    assert k - abs(k)*1.0e-10 <= l <= k + abs(k)*1.0e-10

    m = np.linalg.inv(A_invers1)
    n = ind.invers(A_invers1)
    for row in range(r12):
        for col in range(r12):
            assert m[row][col] - abs(m[row][col])*1.0e-10 <= n[row][col] <= m[row][col] + abs(m[row][col])*1.0e-10
    o = np.linalg.inv(A_invers2)
    p = ind.invers(A_invers2)
    for row in range(r13):
        for col in range(r13):
            assert o[row][col] - abs(o[row][col])*1.0e-10 <= p[row][col] <= o[row][col] + abs(o[row][col])*1.0e-10
    assert ind.invers([[4, 5, 1, 1],[-3, 4, 7, 1],[3, 13, 10,1],[2,1,-1,1]]) == None #Kolumnerna 1,2 och 3 är linjärt beroende

    print('working')

test()

'''I samtliga funktioner förutom matrix_check() från Ind_projekt.py genereras slumpmässiga
matriser där elementen i den är decimaltal. Returvärderna från mina skapade funktioner och
pythons inbyggda linjär algebra modul numpy jämförs. Om skillnaden är
försumbart liten skrivs 'working' ut i terminalen'''
