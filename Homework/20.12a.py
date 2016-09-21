#!/usr/bin/python3.5
# Sorry for documentaion
# But i can`t doc this
#
#
#
import numpy as np
import input_matrix
n = (int(input("Number of elements")))
matrix = input_matrix.create_matrix(n)
indicator = 0
for i in range(0,n):
    for j in range(i+1,n):
        if matrix[i][j] != 0:
            indicator +=1 
#print(matrix)
if indicator != 0:
    print("Not upper triangular matrix")
else:
    print("upper triangular matrix")
