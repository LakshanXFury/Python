"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""

def spiral_order(matrix):
    row = len(matrix)
    col = len(matrix[0])

    total_elements = row * col
    print(total_elements)

    ans = []
    c = 0
    colstart = 0
    rowstart = 0
    colend = col - 1
    rowend = row - 1

    while c < total_elements:
        # rowstart , colstart -> colend
        for i in range(colstart, colend + 1):
            ans.append(matrix[rowstart][i])
            c += 1
        rowstart += 1

        if c == total_elements:
            break

        # colend, rowstart -> rowend
        for i in range(rowstart, rowend + 1):
            ans.append(matrix[i][colend])
            c += 1
        colend -= 1

        if c == total_elements:
            break

        #rowend, colend -> colstart
        for i in range(colend, colstart - 1, -1):
            ans.append(matrix[rowend][i])
            c += 1
        rowend -= 1

        if c == total_elements:
            break

        # colstart, rowend -> rowstart
        for i in range(rowend, rowstart - 1, -1):
            ans.append(matrix[i][colstart])
            c+=1
        colstart += 1

    print(ans)

spiral_order([[1,2,3],[4,5,6],[7,8,9]])
spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

