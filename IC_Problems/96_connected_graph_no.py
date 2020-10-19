
import collections

# Directed graph OR un-directed graph?
# List of tuples - consider the case of single node with in/out degree == 0.
# dfs function better to define as closure.
def build_graph(L):
    graph = collections.defaultdict(list)

    for elem in L:
        # L = [(1,2), (1,4), (3,)]
        if len(elem) >= 2:
            graph[elem[0]].append(elem[1])
            graph[elem[1]].append(elem[0])
        else:
            graph[elem[0]]

    return graph

def connected_components(L):
    graph = build_graph(L)

    def dfs(graph, node):
        state[node] = 'G'
        for nei in graph[node]:
            if state[nei] == 'W':
                dfs(graph, nei)
        state[node] = 'B'

    state = {node : 'W' for node in graph}
    connected_components_in_graph = 0

    for node in graph:
        if state[node] == 'W':
            dfs(graph, node)
            connected_components_in_graph += 1

    return connected_components_in_graph

if __name__ == "__main__":
    L = [(1,2), (1,4), (3,)]
    print (connected_components(L))
