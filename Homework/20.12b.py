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
matrix = np.transpose(matrix)
for i in range(0,n):
    for j in range(i+1,n):
        print(i,j)
        if matrix[i][j] != 0:
            indicator +=1 
if indicator != 0:
    print("Not lower triangular matrix")
else:
    print("Lower triangular matrix")

