import collections

def min_steps_to_unlock_circular_lock(dead_positions, target):

    def neighbour(lock_state):
        for pos in range(len(lock_state)):
            # Silly mistake - first : was missed.
            yield ( lock_state[:pos] + str((int(lock_state[pos]) + 1) % 10) + lock_state[pos+1:])
            yield ( lock_state[:pos] + str((int(lock_state[pos]) - 1) % 10) + lock_state[pos+1:])

    Q = collections.deque()
    visited = []
    visited.append('0000')
    Q.append(('0000', 0))

    while Q:
        item, steps = Q.popleft()
        # dead_positions check was missed.
        if item in dead_positions:
            continue
        if item == target:
            return (True, steps)
        for nei in neighbour(item):
            #print (nei)
            if nei not in visited:
                visited.append(nei)
                Q.append((nei, steps+1))
    return (False, -1)

if __name__ == "__main__":
    dead_positions = ["0201","0101","0102","1212","2002"]
    target = "3238"
    print (min_steps_to_unlock_circular_lock(dead_positions, target))
