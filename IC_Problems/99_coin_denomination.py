
def get_no_of_ways_coin_can_make(coins, X):
    table = [[0]*(X+1) for _ in range(len(coins)+1)]

    for i in range(len(table)):
        table[i][0] = 1

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            # Here you need to use the (***) if you use if else.
            table[i][j] = (table[i-1][j-coins[i-1]] if j >= coins[i-1] else 0) + table[i-1][j]

    #print (table)
    return table[-1][-1]

if __name__ == "__main__":
    coins = [1, 2, 3, 5]
    X = 8

    print (get_no_of_ways_coin_can_make(coins, X))
