
def min_swap_couples(row):

    pairs = {person : pos for pos, person in enumerate(row)}
    swap = 0

    def get_my_neighbour(person):
        return (person-1 if person & 0x1 else person+1)

    def swap_update_persons(pos1, pos2):
        pairs[row[pos1]] = pos2
        pairs[row[pos2]] = pos1
        row[pos1], row[pos2] = row[pos2], row[pos1]

    for pos in range(1, len(row), 2):
        my_neighbor = get_my_neighbour(row[pos-1])
        if my_neighbor != row[pos]:
            swap_update_persons(pos, pairs[my_neighbor])
            swap += 1
    return swap

if __name__ == "__main__":
    row = [0, 3, 5, 2, 1, 4]
    print (min_swap_couples(row))
