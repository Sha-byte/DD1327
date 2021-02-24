 ##    Pseudokod

    function sort_int(v):
        if v is not type list return None

        create an empty list called w
        store the length of v in the variable n
        m = 0
        a = 0
        create a row vector with length n, only containing zeros
        create an empty dictionary called dictionary
        for i from 0 to n:
            if v[i] is a key to dictionary the value of that key will be incremented by 1
            Otherwise the key does not exist and the key will be created with value 1.

        for i in the keys dictionary
            add i to the end of the list w
        
        a function merge(w) will be called and perform mergesort on w

        for k in the list w
            for i from 0 to the value of dictionary with the inserted key k. This is then subtracted by 1.
                output[m] = w[a]
                m is incremented by 1
             a is inremented by 1
        return output
                


    function merge(w):
        if the length of w from sort_int() is bigger than 1:
            w will be divided into one left list and one right list with equal length +-1

        call merge(left) the left list will be input
        call merge(right) the right list will be input
        Every left and right subarray that can possibly be created will be examined by these calls.

        v_counter = 0
        h_counter = 0
        counter = 0

        while h_counter is less than the length of h_list and v_counter is less than the length of v_list:
            if v_list[v_counter] is less than or equal to h_list[h_counter]
                 assign input_list[counter] to v_list[v_counter]
                 v_counter is incremented by 1
            in all othe cases do the same for the right list but replace v_counter with h_counter.
        counter is incremented by 1

        while v_counter is less than the length of the left list variable v_list
            input_list[counter] is assigned to v_list[v_counter]
            v_counter is incremented by 1
        counter is incremented by 1

        while h_counter is less than the length of the left list variable h_list
            input_list[counter] is assigned to h_list[h_counter]
            h_counter is incremented by 1
            counter is incremented by 1
        return


The input_list in merge() that is examined in the while loop above will at first be 
of length two, then the sorted list of those two numbers will be assigned to left 
or right depending on the function call. As we move higher up the stack the left 
and right lists continue to get sorted by the function calls merge(left) and 
merge(right) and we just plug in the numbers from these sorted lists left and 
right into input_list.

Komplettering:
Algoritmen ovan blir linjär om mergesort algoritmen har tidskomplexiteten 
c* k*log_2(k) = O(n), där k naturligtvis är antalet olika tal i input listan v. 
För att detta ska vara möjligt måste input listan v till sort_int innehålla 
flera av samma element. Detta kan ske t.ex om lösningen till olikheten 
k * log_2(k) <= n tillfredställs för listan.