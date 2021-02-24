#### Besök noderna i den här grafen i DFS- och BFS-ordning med start i nod 1. I vilken ordning besöks noderna i de två fallen? Du kan anta att grannarna till en nod besöks i nummerordning.

För depth first search kommer noderna besökas i ordningen 1 -> 2 -> 3 -> 4 -> 5 -> 6
eller kanterna:
{1,1}->{1,2}->{2,3}->{3,4}->{4,5}->{4,6}->{2,5}->{1,5}

För breath first search besöks noderna i ordningen: 

1->2->5->3->4->6


#### Tidskomplexiteten för DFS blir i vissa fall mycket bättre om man använder närhetslistor i stället för en närhetsmatris. Varför då?

En närhetslista kan representeras som en dictionary i python med t.ex: 

    graf = {1: set([1, 2, 5]), 
         2: set([1, 3, 5]),
         3: set([2, 4]),
         4: set([3, 5, 6]),
         5: set([1, 2, 4]),
         6: set([4])}


I detta fall ges grannarna till en nod a av graf[a]. Medan i en närhetsmatris måste alla rader till en kolumn a av matrisen gås igenom för att få fram grannarna till noden a. I en graf med |V| element kommer då |V| rader gås igenom för att få fram grannarna till noden a. Eftersom n noder i grafen kommer gås igenom så blir tidskomplexiteten O(|V|^2) för närhetsmatrisen och O(|V| + |E|), för närhetslistan där |E| är antalet kanter i grafen. 

#### För vilken typ av grafer blir den asymptotiska tidskomplexiteten för DFS den samma för båda datastrukturerna?

Vi betraktar en enkel graf med |V| - a kanter från varje nod till andra noder. De respektive närhetslistorna till noderna kommer alla att innehålla |V| - a kanter. För varje nod som gås igenom kommer |V|-a element besökas i en närhetslista och tidskomplexiteten blir då O(|V|*(|V|-a)) + O(|V|) = O(|V|*a + |V|^2), om a väljs litet blir uttrycket O(|V|^2) vilket är samma tidskomplexitet som den för en närhetsmatris. Om grafen innehåller många kanter (nära |V| kanter) från varje nod kommer den asymptotiska tidskomplexiteten bli samma för närhetsmatriser som för närhetslistor dvs O(|V|^2).