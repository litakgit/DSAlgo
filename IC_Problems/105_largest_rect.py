
import copy

def get_largest_rect_under_histogram(H):
    largest_rect_area = 0
    stack = []
    for pos, height in enumerate(H):
        while stack and H[stack[-1]] >= height:
            stack.pop()
        width = pos+1 if not stack else pos - stack[-1]
        largest_rect_area = max(largest_rect_area, height * width)
        stack.append(pos)
    return largest_rect_area

def get_largest_rect(matrix):
    histo = copy.deepcopy(matrix)
    max_rect = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if histo[row][col] == 0:
                histo[row][col] = 0
            else:
                histo[row][col] = (histo[row-1][col] + histo[row][col] if row > 0
                                    else histo[row][col])
    for row in histo:
        rect = get_largest_rect_under_histogram(row)
        #print (row, rect)
        max_rect = max(max_rect, rect)

    return max_rect

if __name__ == "__main__":
    matrix = [[0,0,1,1,0], [1,1,1,1,1], [1,1,1,1,1], [0,1,1,1,1]]
    matrix = [[0]]
    print (get_largest_rect(matrix))
