#!usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    :param matrix: 2 dimensional array
    :return: a new matrix with each value being the square of 
    the value of the input
    """

    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    # Compute the square value of each integer in the input matrix
    # and store it in the new matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
