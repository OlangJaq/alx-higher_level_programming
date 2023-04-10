#!/usr/bin/pythonet
"""a function to multiply matrix using numpy"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """multiply matrix"""
    result = np.dot(m_a, m_b)
    return result

