
# abc | axb

def get_edit_distance(word1, word2):
    # declares a table with word1 as coloumns and word2 as rows.
    table = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
    for i in range(len(word2)+1):
        table[i][0] = i
    for i in range(len(word1)+1):
        table[0][i] = i

    for row in range(1, len(word2)+1):
        for col in range(1, len(word1)+1):
            # Check the i,j th positions of the words. Note that index is less than 1.
            if word2[row-1] == word1[col-1]:
                table[row][col] = table[row-1][col-1]
            else:
                table[row][col] = min(table[row-1][col-1],
                                      table[row-1][col],
                                      table[row][col-1]) + 1

    # Last elem of the table. If any of the word is None, then row/col not defined.
    # So use lengths of the word to get the last entry in the table.
    return table[len(word2)][len(word1)]



if __name__ == "__main__":
    print (get_edit_distance("abc", ""))
    print (get_edit_distance("", "abc"))
    print (get_edit_distance("abc", "abc"))
