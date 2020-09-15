import collections
import heapq

# 0 1 2 3 4 5 6 7 
# a b a e a c a a
# z z z b m a q a
# c b a a p a q a
def get_largest_lexi_string(A, B):
    a_list, b_list, res = [], [], []
    last_pos = -1
    for i,c in enumerate(A):
        a_list.append((c, i))
    a_list.sort(key=lambda a: (a[0], not a[1]), reverse=True)
    print (a_list)
    # [('c', 3), ('b', 1), ('b', 5), ('a', 0), ('a', 2), ('a', 4), ('a', 6), ('a', 7)]
    #import pdb; pdb.set_trace()
    last_pos = start_pos = a_list[0][1]
    res.append(a_list[0][0])
    b_list.append(B[last_pos])
    for item in a_list[1:]:
        if item[1] > last_pos:
            if item[0] >= B[start_pos]:
                res.append(item[0])
                last_pos = item[1]
                b_list.append(B[last_pos])
            else:
                break
    res.extend(b_list)
    print (''.join(res))

def sort_increasing(A):
    write_index = 1
    for i in range(1,len(A)):
        if A[i][1] > A[write_index - 1]:
            A[write_index] = A[i]
            write_index += 1
    del A[write_index:]

def build_graph_from_list(A):
    g = collections.defaultdict(list)
    for elem in A:
        g[elem[0]].append((elem[1], elem[2]))
    return g

def least_time_to_travel_signal(graph, k):
    pq = []
    visited = []
    heapq.heappush(pq, (0, k))
    max_time_till_now = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        max_time_till_now = max(max_time_till_now, cost)
        visited.append(node)
        for nei_dest, nei_cost in graph[node]:
            if nei_dest not in visited:
                heapq.heappush(pq, (cost + nei_cost, nei_dest))

    return -1 if len(visited) != len(graph.keys()) else max_time_till_now


if __name__ == "__main__":
    #get_largest_lexi_string("abaeacaa", "zzzamaqa")
    #get_largest_lexi_string("ab", "zy")
    #graph = build_graph_from_list([[2,1,10], [2,3,1], [3,4,1], [4,1,1], [5, 4, 1]])
    import pdb; pdb.set_trace()
    graph = build_graph_from_list([[1,2,1],[2,3,7],[1,3,4],[2,1,2]])
    time = least_time_to_travel_signal(graph, 1)
    print ("Time taken {}".format(time))
