#!usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    :param matrix: 2 dimensional array
    :return: a new matrix with each value being
    the square of the value of the input
    """

    # Create a new matrix with the same size as the input matrix
    new_matrix = [[x**2 for x in row] for row in matrix]
    return(new_matrix)
