def dfs_caller(graf):
    marked = set()
    alla_elever = set(graf)
    ut = {}
    while alla_elever - marked != set():
        for elev in alla_elever - marked:
            break
        ut.update(_dfs(graf, elev, marked, {}))

    return ut


def _dfs(graf, current, marked, output):
    if output == {}:
        output[current] = 1
    marked.add(current)
    store = graf[current] - marked


    for next in store:
        if output.get(next) != None:
            if output[current] == output[next]:
                print(current + ' och ' + next + ' går inte att få ihop')
        elif output[current] == 1:
            output[next] = 2
        else:
            output[next] = 1
        _dfs(graf, next, marked, output)
    return output


"""Närhetslistor:"""
graf1 = {'Adam':set(['Emil','Greta', 'David']),
    'Beatrice': set(['Greta','Emil', 'David']),
    'Calle': set(['Emil']),
    'David': set(['Adam','Beatrice']),
    'Emil': set(['Frida','Adam','Beatrice','Calle']),
    'Frida': set(['Emil']),
    'Greta': set(['Adam','Beatrice']),
    'peter': set(['Sanna', 'Clara']),
    'Sanna': set(['peter', 'My', 'Karl']),
    'Clara': set(['peter', 'Martin']),
    'My': set(['Sanna']),
    'Karl': set(['Sanna', 'Martin']),
    'Martin': set(['Clara', 'Karl'])}


print(dfs_caller(graf1))
