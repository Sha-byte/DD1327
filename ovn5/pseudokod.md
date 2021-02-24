    public function dfs_caller(graf):
        assign marked to an empty set
        assign alla_elever to a set containing the strings representing the names of all the students
        assign ut to an empty dictionary
        while alla_elever is containing elements that marked is not containing:
            assign the variable elev to any string that is in the set alla_elever but not in the set marked:
            add the output of _dfs(graf, elev, marked, {}) to the variable ut
            '''ut will at the end represent a key value pair with all the keys being
            the names of the students and the values being test type 1 or 2.'''
            return ut
 





    private function _dfs(graf, current, marked, output)
        if this is the first vertex in this subgraph that you visit:
            assign output[current] to 1 #The first person has test type 1
        add current to the set
        Create a variable store which is a set containing the neigbors of current except for the ones that has already been visited
        for next in store:
            if output[next] exist and is equal to output[current]:
                print( current + ' och ' + next + ' går inte att få ihop')
            elif output[current] is equal to 1:
                assign output[next] to 2
            else:
                output[next] is equal to 1
             
            _dfs(graf, current, marked, output)
        return output


"""Variabeln output under den privata funktionen _dfs() kan representeras som 
en dictionary i python och innehåller namnen på eleverna som nycklar och 
de korresponderande värderna är vilken provtyp eleven får i de respektive delgraferna. Alla key value pairs 
från delgrafer sparas i en enda variabel som jag kallar ut. Algoritmen ovan kommer gå igenom alla
kanter i grafen så om nästa som ska besökas redan har besökts och den noden hade samma provtyp som
den nuvarande noden då kommer det skrivas ut i terminalen att de inte går att få ihop.
Strängarna som är namnen på eleverna och de som känner varandra är tillgängliga 
i en närhetslista som representeras av variabeln graf i 
pseudokoden ovan. Tidskomplexiteten för algoritmen ovan blir
densamma som den för depth first search med en närhetslista och är O(|E| + |V|),
där |E| är antalet kanter och |V| är antalet hörn i grafen. Jag skrev mer om det i uppgift 3."""