#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer
"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []
    final_list = [[1]]
    for x in range(n-1):
        temp = [0] + final_list[-1] + [0]
        new_list = []
        for y in range(len(final_list[-1]) + 1):
            new_list.append(temp[y] + temp[y+1])
        final_list.append(new_list)
    return final_list
