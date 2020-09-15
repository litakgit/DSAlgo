topo_stack = []
state = {}
tickets = {'DEL':'KOL', 'MUM':'DEL', 'BLR':'MUM'}

def dfs(graph, start):
    state[start] = 'G'
    for nei in neighbour(graph, start):
        if state[nei] == 'W':
            dfs(graph, nei)
    state[start] = 'B'
    topo_stack.append(start)

def topological_sort(graph):
    for node in graph.keys():
        state[node] = 'W'
    for node in graph.keys():
        if state[node] == 'W':
            dfs(graph, node)
    return topo_stack

def get_itinerary(graph):
    plan = []
    topological_sort(graph)
    while topo_stack:
        location = topo_stack.pop()
        plan.append(location)
    return plan

if __name__ == "__main__":
    g = build_graph()
    get_itinerary(g)
