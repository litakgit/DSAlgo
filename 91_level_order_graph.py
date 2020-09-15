
import collections

def get_level_order_nodes(g, start):
    """
    Lessons:
        - Missed the param in defaultdict.
        - visited.append was missing.
    """

    visited = []
    Q = collections.deque()
    Q.append(start)
    visited.append(start)

    res = []

    while Q:
        item = Q.popleft()
        res.append(item)
        for nei in g[item]:
            if nei not in visited:
                visited.append(nei)
                Q.append(nei)
    return res


if __name__ == "__main__":
    g = collections.defaultdict(list)
    g[1].append(2)
    g[1].append(3)
    g[2].append(4)
    g[3].append(5)

    print (g)

    print (get_level_order_nodes(g, 1))
