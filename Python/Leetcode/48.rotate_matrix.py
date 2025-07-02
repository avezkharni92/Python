def rotate(matrix):
    # TODO
    #start a for loop for going through the matrix row and then column
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            #print(matrix)
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()
            
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)


def rotate(matrix):
    n = len(matrix)
    # Create a new matrix of the same size, initialized with 0s
    new_matrix = [[0] * n for _ in range(n)]
    
    # Perform the rotation by assigning values from the original matrix
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - i - 1] = matrix[i][j]
    
    return new_matrix

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = rotate(matrix)
print(new_matrix)
