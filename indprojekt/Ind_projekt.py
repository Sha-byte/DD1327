# -*- coding: <utf-8> -*-
import numpy as np
'''Modulen ovan används endast för input matriser/arrays av typen np.ndarray. Modulen måste
importeras för att översättaren i python ska förstå vad np.ndarray är när funktionen matrix_check
som beskrivs nedan anropas'''


def matrix_check(m):
    """matrix_check kontrollerar om input matrisen verkligen är en matris och returnerar en lista
    som innehåller antalet rader och kolumner i inputmatrisen m. Annars returneras False"""
    if isinstance(m, (np.ndarray, list)):
        if isinstance(m[0], (np.ndarray, list)):
            antal_rader = len(m) #O(1)
            antal_kolumner = len(m[0])
            for rad_nr in range(antal_rader):
                if antal_kolumner == len(m[rad_nr]):
                    for kolumn_nr in range(antal_kolumner):
                        if isinstance(m[rad_nr][kolumn_nr], (float, int, np.float64, np.int64)):
                            pass
                        else:
                            return False
                else:
                    return False
            return [antal_rader, antal_kolumner]
        else:
            return False
    else:
        return False
"""Tidskomplexiteten är O(n*m), n är antalet rader och m antalet kolumner. Detta är p.g.a att vi
måste kontrollera att varje enskilt element i matrisen är av antingen typen float eller integer"""


def matrix_addition(m1, m2):
    """matrix_addition() tar två matriser som input och returnerar summan av dem."""
    m_sum = []
    m1_info = matrix_check(m1)
    m2_info = matrix_check(m2)
    if (m1_info and m2_info) and (m1_info == m2_info):
        antal_rader = m1_info[0]
        antal_kolumner = m1_info[1]
        for rad_nr in range(antal_rader):
            m_sum.append([]) # O(1)
            for kolumn_nr in range(antal_kolumner):
                m_sum[rad_nr].append(m1[rad_nr][kolumn_nr] + m2[rad_nr][kolumn_nr])
        return m_sum
    else:
        return False

""" Tidskomplexiteten blir O(n*m), där n är antalet rader och m antalet kolumner"""

def scalar(s, m): #Skalär s multiplicerat med matris m
    """scalar() tar en integer eller float (s) som input och en matris (m) som input och
    returnerar värdet av skalären (s) multiplicerat med matrisen (m)."""
    m_info = matrix_check(m)
    m_s = []
    if (type(s) == int or type(s) == float) and m_info:
        for rad in range(m_info[0]):
            m_s.append([])
            for kolumn in range(m_info[1]):
                m_s[rad].append(s*m[rad][kolumn])
        return m_s
    else:
        return False
"""Tidskomplexiteten blir O(n*p), där n är antalet rader och p antalet kolumner"""

def matrix_multiplication(m1, m2):
    '''matrix_multiplication() tar matriserna m1 och m2 som input och beräknar m1 multiplicerat med m2.
    För att matrismultiplikationen ska fungera måste m1 vara pxn och m2 nxm enligt definitionen på matrismultiplikation'''
    m_product = []
    m1_info = matrix_check(m1)
    m2_info = matrix_check(m2)
    if (m1_info and m2_info) and (m1_info[1]  == m2_info[0]):
        antal_rader = m1_info[0]
        antal_kolumner = m2_info[1]
        for rad in range(antal_rader):
            m_product.append([])
            for kolumn in range(antal_kolumner):
                m_product[rad].append(0)
                for element_nr in range(m1_info[1]):
                    m_product[rad][kolumn] += m1[rad][element_nr]*m2[element_nr][kolumn]
        return m_product
    else:
        return False
''' Om m1 är mxp och m2 är pxn, då är tidskomplexiteten för algoritmen ovan
O(n*m*p). Jag tror inte det går att få fram snabbare tidskomplexitet än så eftersom alla operationer under for
looparna är nödvändiga'''

def transponat(m):
    '''transponat() returnerar transponatet av input matrisen m.'''
    m_info = matrix_check(m)
    m_trans = []
    if m_info:
        for kolumn in range(m_info[1]):
            m_trans.append([0]*m_info[0])
            for rad in range(m_info[0]):
                m_trans[kolumn][rad] = m[rad][kolumn]
        return m_trans
    else:
        return  False
'''transponat() beräknar transponatet av input matrisen m. Det innebär att en matris m_trans returneras där varje
element är m_trans[row][column] = m[column][row]. Om m är pxn så är retur matrisen m_trans nxp. Tidskomplexiteten
blir O(n*m), där n är antalet rader och m är antalet kolumner av matrisen m'''

def determinant(m):
    '''determinant() returnerar determinanten av input matrisen m.'''
    m_info = matrix_check(m)
    m_det = m.copy()
    '''Jag gör rad operationer på m för att få matrisen i övre triangulär form.'''
    if m_info[0] == m_info[1]:
        n = m_info[0]
        for diagonal in range(n):

            for rad in range(diagonal+1,n):
                '''Jag betraktar endast rader under diagonal.'''
                if m_det[diagonal][diagonal] == 0:
                    m_det[diagonal][diagonal] == 1.0e-30
                '''m_det[diagonal][diagonal] == 1.0e-30 eller m_det[diagonal][diagonal] == 0 kommer inte
                göra någon skillnad i vad det resulterande värdet på determinanten blir, se testkoden'''

                faktor = m_det[rad][diagonal] / m_det[diagonal][diagonal]
                '''Nuvarande raden (rad) - faktor * nuvarande diagonalraden'''
                for kolumn in range(n):
                    m_det[rad][kolumn] = m_det[rad][kolumn] - faktor * m_det[diagonal][kolumn]
        det = 1.0
        '''Produkten av diagonalerna är av m i övre triangulär form = m_det är produkten av
        diagonalerna i m_det'''
        for i in range(n):
            det *= m_det[i][i]
        return det
    else:
        return False
'''determinant() beräknar determinanten av input matrisen m. Om input matrisen inte är kvadratisk så returneras False.
Tidskomplexiteten för determinant() är O(n^3),
detta är högt men troligtvis den bästa tidskomplexiteten man kan få. Det blir t.ex betydligt sämre
tidskomplexitet för en rekursiv algoritm som stryker rader och kolumner för att få fram determinanten'''

def invers(m):
    ''''invers() beräknar och returnerar inversen av input matrisen m om den existerar, annars returneras
    None.'''
    m_info = matrix_check(m)
    '''Jag gör rad operationer på m för att få matrisen i övre triangulär form.'''
    if m_info[0] == m_info[1]:
        n = m_info[0]
        m_copy = m.copy()
        m_inv = []
        for identiy_matrix in range(n):
            m_inv.append([0]*n)
            m_inv[identiy_matrix][identiy_matrix] = 1
        for diagonal in range(n):

            for rad in range(diagonal+1,n):
                '''Jag betraktar endast rader under diagonal.'''
                index = diagonal
                while m_copy[index][diagonal] == 0:
                    if index == n - 1:
                        return None
                    index += 1
                if index != diagonal:
                    m_copy[diagonal][:], m_copy[index][:] = list(m_copy[index][:]), list(m_copy[diagonal][:])
                    m_inv[diagonal][:], m_inv[index][:] = list(m_inv[index][:]), list(m_inv[diagonal][:])
                '''Om elementet i diagonalen är 0. Byt plats på raden med diagonalen och en rad som har ett
                element som inte är noll i samma kolumn'''
                faktor = m_copy[rad][diagonal] / m_copy[diagonal][diagonal]
                '''Nuvarande raden (rad) - faktor * nuvarande diagonalraden'''
                for kolumn in range(n):
                    m_copy[rad][kolumn] = m_copy[rad][kolumn] - faktor * m_copy[diagonal][kolumn]
                    m_inv[rad][kolumn] = m_inv[rad][kolumn] - faktor * m_inv[diagonal][kolumn]

        if m_copy[n-1][n-1] == 0:
            return None
        else:
            '''m_copy är nu i övre triangulär form. Jag behöver endast
            subtrahera bort elementen över diagonalen av m_copy och skala elementen i diagonalen för
            att m_copy ska bli en identitetsmatris.'''
            for index in range(1,n+1):
                for row in range(n - index, -1, -1):
                    if row == n - index:
                        diagonal = m_copy[n - index][n - index]
                        for col in range(n):
                            m_copy[row][col] = m_copy[row][col]/diagonal
                            m_inv[row][col] = m_inv[row][col]/diagonal
                    else:
                        skalare =  m_copy[row][n - index]
                        for col in range(n):
                            m_copy[row][col] = m_copy[row][col] - skalare*m_copy[n - index][col]
                            m_inv[row][col] = m_inv[row][col] - skalare*m_inv[n - index][col]
            return m_inv


    else:
        return None
'''Tidskomplexiteten ovan blir O(n^3), detta kan en se genom att räkna for looparna under varandra.
O(n^3) är ganska högt men troligtvis den bästa tidskomplexiteten som kan fås då algoritmen ovan är samma
algoritm jag hade använt vid beräkning av inversen för hand.'''
