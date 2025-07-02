#Given 2D list calculate the sum of diagonal elements

def diagonal_sum(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum += matrix[i][j]
    return sum

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum(matrix))

def diagonal_sum1(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
                sum += matrix[i][i]
    return sum

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonal_sum1(matrix))