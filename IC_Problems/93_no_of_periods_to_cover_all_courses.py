import collections

def build_graph(course_dependancy_list):
    graph = collections.defaultdict(list)
    for elem in course_dependancy_list:
        graph[elem[0]].append(elem[1])
        # NOTE : Without this graph dd will be updated in dfs and
        # that will cause RunTime Error of dictionary updated
        graph[elem[1]]
    return graph

def topological_sort(course_graph):
    def dfs(node):
        state[node] = 'G'
        for nei in course_graph[node]:
            if state[nei] == 'W':
                dfs(nei)
        state[node] = 'B'
        topo_stack.append(node)

    topo_stack = []
    # stuck here : how to define all the nodes?
    # in build_graph : graph[elem[1]] does the tric
    state = {node: 'W' for node in course_graph}

    for node in course_graph:
        if state[node] == 'W':
            dfs(node)

    return topo_stack

def get_course_periods(topo_stack, course_graph):
    course_to_periods = {node:0 for node in course_graph}

    while topo_stack:
        elem = topo_stack.pop()
        for nei in course_graph[elem]:
            course_to_periods[nei] = max(course_to_periods[nei], course_to_periods[elem]+1)

    return course_to_periods

def get_max_periods(course_list):
    course_graph = build_graph(course_list)
    topo_stack = topological_sort(course_graph)
    course_to_periods = get_course_periods(topo_stack, course_graph)
    return max(course_to_periods.values()) if course_to_periods else 0

if __name__ == "__main__":
    courses = [(1,2), (2,3), (2,4), (4,5), (3,5), (6,7), (6,8), (7,8)]
    courses = [(1,2)]
    print (get_max_periods(courses))

