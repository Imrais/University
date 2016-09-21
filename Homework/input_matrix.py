#!/usr/bin/python3.5
# Sorry for documentaion
# But i can`t doc this
# How you can see this for inputing of square
# matrix and creating of 2-demensional numpy
# array from it
#
import numpy as np
def create_matrix(n):
    matrix = []
    for i in range(0,n):
        s = input()
        s = s.split()
        #assert s.len == n, "Error"
        s = map(int,s)
        s = list(s)
        matrix.append(s)
    matrix = np.array(matrix)
    return matrix
if __name__ == '__main__':
    n = int(input("Number of elements in row/column"))
    matrix = input_matrix(n)
    print(matrix)
