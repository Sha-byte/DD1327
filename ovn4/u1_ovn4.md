## Övning 4 uppgift 1

#### Teori:
    def pow(n):
	"""Return 2**n, where n is a nonnegative integer."""
	    if n == 0:
		    return 1
	    x = pow(n//2)
	    if n%2 == 0:
		    return x*x
	    return 2*x*x

Funktionen pow(n) kommer att anropas k ggr i rad 5 till koden ovan. 2^k = n &rArr; log_2(n) = k. 
Värstatidskomplexiteten för ovan är O(log(n)).
                                             
                                    
    def sum1(a):
	"""Return the sum of the elements in the list a."""
	    n = len(a)
	    if n == 0:
		    return 0
	    if n == 1:
		    return a[0]
	    return sum1(a[:n//2]) + sum1(a[n//2:])                                    

Den inbyggda slice funktionen i python har en tidskomplexitet O(n/2) i fallen 
ovan för a[:n//2] och a[n//2:]. Om man ritar upp ett funktions anrops träd 
för en lista a med 2^m element där m är något positivt heltal kan man lätt se 
att antalet operationer och tidskomplexiteten är proportinellt mot k*n där 
2^k = n &rArr; k = log_2(n) därmed har jag att tidskomplexiteten är 
O(n*log(n)). Samma princip som ovan gäller såklart även när a innehåller 
något annat än 2^m element, men det är betydligt lättare att se i ett 
funktionsanropsträd när a innehåller 2^m element.


    def sum2(a):
	    """Return the sum of the elements in the list a."""
	    return _sum(a, 0, len(a)-1)

    def _sum(a, i, j):
	"""Return the sum of the elements from a[i] to a[j]."""
	    if i > j:
		    return 0
	    if i == j:
		    return a[i]
	    mid = (i+j)//2
	    return _sum(a, i, mid) + _sum(a, mid+1, j) 
Här använder _sum en liknande algoritm som sum1 gjorde . En kan se här att när antalet 
element som listan a innehåller fördubblas 
kommer också antalet operationer att fördubblas. Värstatidskomplexiteten för _sum är O(n).

                                                                                                                


#### Praktik:
Tid mäts i sekunder nedan

För funktionen pow():

| n | Time |
| --- | ----------- |
| 10 | 3.0994415283203125e-06 |
| 100 | 3.814697265625e-06 |
|1000|  6.9141387939453125e-06|
|10000| 2.5033950805664062e-05|
|100000| 0.0002968311309814453|
|1000000| 0.004179239273071289|

För funktionen sum1():

| Antal listelement | Time |
| --- | ----------- |
| 10 | 1.0967254638671875e-05 |
| 100 | 6.198883056640625e-05 |
|1000|  0.0005829334259033203|
|10000| .005568981170654297|
|100000| 0.058175086975097656|
|1000000| 0.5986661911010742|


För funktionen sum2():

| Antal listelement | Time |
| --- | ----------- |
| 10 | 6.9141387939453125e-06 |
| 100 | 5.507469177246094e-05 |
|1000|  0.00046181678771972656|
|10000| 0.004517078399658203|
|100000| 0.03957390785217285|
|1000000| 0.4089059829711914|

#### Disskusionsdel:
Ordonotationen används som ett mått eller approximation på hur ett program 
kommer bete sig då det är en stor mängd data som ska köras i en funktion 
(dvs när det kommer ta långt tid). I fallet för funktionen  ovan är datan så 
pass liten att uttrycken för tidskomplexiteten inte nödvändigtvis kommer 
vara intressant. Därmed om input datamängden hade varit stor så hade 
tidskomplexiteten varit betydligt mer intressant. Vissa operationer tar t.ex 
längre tid än andra men när man räknar teoretiskt räknar man det som att det 
tar lika långt tid. T. ex tar det längre tid att räkna 10000/12  än att 
räkna 1/2.

Komplettering till diskussionsdelen:
En annan sak som är värd att påpeka när man beräknar tidskomplexiteten är 
att t.ex behöver inte O(n*log(n)) säga så mycket om tiden det tar att köra 
eftersom O(n*log(n)) kan innebära att tiden är proportionellt mot n*log(n)
eller 10000 * n * log(n) detta är en stor skillnad som inte tas hänsyn till 
vid beräkning av teoretisk tidskomplexitet. Sen som jag nämnde lite ovan så 
tar även vissa operationer som är t.ex O(1) längre tid än andra som också är 
O(1) t.ex är 1000 = O(1).

För funktionen pow() fick jag följande praktiska värden på kör tiden:

| n | Time |
| --- | ----------- |
| 10 | 3.0994415283203125e-06 |
| 100 | 3.814697265625e-06 |
|1000|  6.9141387939453125e-06|
|10000| 2.5033950805664062e-05|
|100000| 0.0002968311309814453|
|1000000| 0.004179239273071289|

Tidskomplexiteten jag fick fram var O(log(n)). Tiden som en funktion av n ser 
inte riktigt ut som en logaritmisk funktion dvs a * log_2(n) för någon 
regressionsanpassad konstant a, dock är detta inte så konstigt eftersom n = 1000000 kommer t. ex multiplicera tal x*x och 2//n som är betydligt större än fallet för n = 100000 (framförallt operationerna 2 * x *x och x * x). Därmed kan inte operationen x *x betraktas som likvärdig i de båda fallen om man ska undersöka den praktiska tiden.

sum1:
Samma argument som ovan används även för sum1. T. ex kommer operationen n//2 ta längre tid för t.ex n = 1000 jämfört med n = 100. Det kommer göras betydligt fler operationer på stora tal n på en lista som är av längd 1000000 jämfört med en som är 10000.

sum2:
Återigen ges samma argument. Ett flertalet rekursiva anrop kommer att göras och mid = (i+j)//2
kommer i genomsnitt att ta längre tid att beräknas om listan i input innehåller t.ex 1000000 
element jämfört med en som innehåller 100000.

