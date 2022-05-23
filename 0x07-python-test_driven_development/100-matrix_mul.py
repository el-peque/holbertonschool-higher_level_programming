#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """adds two integers or floats, casting floats into integers"""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if all(isinstance(x, (list)) for x in m_a) == True:
        raise TypeError("m_a must be a list of lists")
    if all(isinstance(x, (list)) for x in m_b) == True:
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or [[]]:
        raise ValueError("m_b can't be empty")

    
