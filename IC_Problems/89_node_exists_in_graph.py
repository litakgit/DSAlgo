import collections

# L = [(1,2), (3,5), (1,5), (6,)]
def get_graph(L):
    graph = collections.defaultdict(list)
    for elem in L:
        if len(elem) > 1:
            graph[elem[0]].append(elem[1])
            graph[elem[1]]
        else:
            graph[elem[0]]
    #print (graph)
    return graph

def check_node_existance(graph, target_node):
    def dfs(g, node, target):
        state[node] = 'G'
        if node == target:
            return True
        for nei in g[node]:
            if state[nei] == 'W'and dfs(g, nei, target):
                return True
        state[node] = 'B'
        return False

    state = {node : 'W' for node in graph.keys()}
    for each_node in graph.keys():
        if state[each_node] == 'W':
            if dfs(graph, each_node, target_node):
                return True

def is_node_exists_in_graph(L, target):
    graph = get_graph(L)
    node_exists = check_node_existance(graph, target)
    return True if node_exists else False

if __name__ == "__main__":
    # (6, ) ~ is a tuple
    # (6) ~ is not a tuple, an integer!
    L = [(1,2), (3,5), (1,5), (6,)]
    result = is_node_exists_in_graph(L, 3)
    if result:
        print ("node found")
    else:
        print ("node NOT found")
