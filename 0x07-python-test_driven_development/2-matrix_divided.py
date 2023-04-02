#!/usr/bin/python3

def matrix_divided(matrix, div):
    """function that divides all elements of a matrix."""
    # Check that matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check that all rows of the matrix have the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    
    return new_matrix
