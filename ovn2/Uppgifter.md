# ovn2
Övning 2

2.1 Ordo-notation:
n + 100 ∈ O(n*log(n)), n*log(n)∈ O(x^(1.5)), x^(1.5) ∈ O(2^n), 2^n ∈ O(10^n)

1. n(n + 1)/2 = O(n 3) är sant eftersom VL har grad två och högerled grad tre.

2. n(n + 1)/2 = O(n^2) är sant eftersom det finns positiva konstanter M sådant att
|VL| <= M |HL| när n går mot oändligt.

3. n(n + 1)/2 = Θ(n^3) är det samma som att säga n(n + 1)/2 >= m * (n^3)
för n > n0 och någon positiv konstant m. Detta är givetvis falskt eftersom VL är grad 2 och
HL är grad 3. Tredjegradspolynom växer snabbare än andragradare för stora n.

4. n(n + 1)/2 = Ω(n) endast om k * n <= n(n+1)/2, för n > n0 och positiv
konstant k.
Detta är sant eftersom en n^2 term kommer växa snabbare än k*n.


2.2 Prefixsumma:

    for i = 0 to n-1
        Add the numbers A[0] thru A[i].
        Store the result in B[i].

• Beräkna tidskomplexiteten för denna algoritm och uttryck den på formen O(f(n)), där
funktionen f(n) är så liten och enkel som möjligt.

Tidskomplexiteten är O(n^2), antalet element är proportionellt mot antalet
operationer upphöjt i två. Detta eftersom antalet operationer under for loopen blir i+1<   
 för varje iteration i for loopen,
i additioner och 1 tilldelning. n + Σi = n + n*(n+1)/2 = n^2/2 + 3/2*n.




• Visa att tidskomplexiteten också är Ω(f(n)).

Dvs visa att T(n) >= m * n. Sätt T(n) = n^2/2 + 3/2*n >= (n^2)/3 om n > 1.


• Hitta på en algoritm med bättre asymptotisk tidskomplexitet. Beskriv algoritmen i
pseudokod och ange dess tidskomplexitet med Θ-notation.

    carry = 0
    for i = 0 to n-1
        Add A[i] to carry.
        Store carry in B[i].

Tiden det tar för programmet att köra koden ovan kan skrivas som a*n, för positiv konstant
a. För 0<b<a<c gäller då att b*n < a*n < c*n för 0 < k < n, därmed är algoritmen ovan Θ(n)

2.4 En ovanlig funktion?
• Ge ett exempel på en positiv funktion f(n) sådan att f(n) varken är O(n) eller Ω(n)

Ett exempel är f(n) = cos(n)^2 + n^2*sin(n)^2. Denna går inte att avgöra om den är större
än eller mindre än k*n för någon positiv konstant k när n går mot oändligt. Därmed är f(n)
varken O(n) eller Ω(n).      
