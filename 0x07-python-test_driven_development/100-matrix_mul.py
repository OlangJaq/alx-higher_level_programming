#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                   or if any element of those list of lists is not an integer or a float,
                   or if each row of m_a or m_b is not of the same size.
        ValueError: If m_a or m_b is empty or if m_a and m_b cannot be multiplied.

    Returns:
        A new matrix as a list of lists.
    """

    # Check if m_a is a list of lists of integers or floats
    if not isinstance(m_a, list) or not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a must be a list of lists of integers or floats")

    # Check if m_b is a list of lists of integers or floats
    if not isinstance(m_b, list) or not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b must be a list of lists of integers or floats")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    # Check if each row of m_a has the same size
    a_cols = len(m_a[0])
    if any(len(row) != a_cols for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Check if each row of m_b has the same size
    b_cols = len(m_b[0])
    if any(len(row) != b_cols for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if a_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(b_cols):
            value = sum([m_a[i][k] * m_b[k][j] for k in range(a_cols)])
            row.append(value)
        result.append(row)

    return result

