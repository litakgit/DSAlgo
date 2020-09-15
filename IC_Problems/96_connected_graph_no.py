import collections

# Given a graph, mark each connected components with different colors.
# This problem boils down to finding the no of connected components only.

def get_no_of_connected_components(g):
    def dfs(g, start):
        state[start] = 'G'
        for nei in g[start]:
            if state[nei] == 'W':
                dfs(g, nei)
        state[start] = 'B'
        return False

    state = {node : 'W' for node in g}
    color = 0

    for node in g:
        if state[node] == 'W':
            color += 1
            dfs(g, node)

    return color

if __name__ == "__main__":
    g = collections.defaultdict(list)
    g[1].append(2)
    g[2].append(1)
    g[1].append(3)
    g[3].append(1)
    g[2].append(4)
    g[4].append(2)
    g[3].append(3)
    g[5].append(6)
    g[6].append(5)
    g[7]
    print (g)
    print (get_no_of_connected_components(g))
