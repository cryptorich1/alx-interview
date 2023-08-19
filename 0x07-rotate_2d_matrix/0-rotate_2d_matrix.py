#!/usr/bin/python3
'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix by 90 degrees clockwise
    """
    size = len(matrix)
    inc = [i for i in range(size)]
    dec = [i for i in range(size - 1, -1, -1)]
    matrix_copy = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j)
        matrix_copy.append(temp)

    for i in range(size):
        for j, k in zip(inc, dec):
            matrix[i][k] = matrix_copy[j][i]
