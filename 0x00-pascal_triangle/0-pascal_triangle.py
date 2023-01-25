#!/usr/bin/python3
'''
Module of Pascal's triangle of n
'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing the Pascal's triangle of n
    '''

    if n <= 0:  # if n is not a positive integer
        return []
    triangle = [[1]]  # initialize the first row of the triangle
    for i in range(1, n):  # for each row in the triangle
        row = [1]  # initialize the first element of the row
        for j in range(1, i):  # for each element in the row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
            # add the two elements to the row
        row.append(1)  # add the last element to the row
        triangle.append(row)  # add the row to the triangle
    return triangle  # return the triangle