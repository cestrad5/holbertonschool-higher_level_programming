#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats, otherwise is error.
    """

    new_mx = []
    Mx_TypeError = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(Mx_TypeError)
    if matrix is None and matrix[0] is None:
        raise TypeError(Mx_TypeError)
    if type(matrix) is not list:
        raise TypeError(Mx_TypeError)
    for lists_inside in matrix:
        if type(lists_inside) is not list:
            raise TypeError(Mx_TypeError)
        for numbers in lists_inside:
            if type(numbers) is not int and type(numbers) is not float:
                raise TypeError(Mx_TypeError)

    if matrix == "" or matrix == " " or matrix is None or not matrix:
        raise TypeError(Mx_TypeError)
    if lists_inside == "" or lists_inside == " " \
            or lists_inside is None or not lists_inside:
        raise TypeError(Mx_TypeError)
    if numbers == "" or numbers == " " or numbers is None or not numbers:
        raise TypeError(Mx_TypeError)

    if not all(len(lists_inside) is len(matrix[0]) for lists_inside in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == "" or div == " " or div is None or not div:
        raise TypeError("div must be a number")

    for lists_inside in matrix:
        new_mx.append(list(map(lambda dv: round(dv / div, 2), lists_inside)))

    return new_mx
