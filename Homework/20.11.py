#!/usr/bin/python3.5
import numpy as np
import input_matrix as in_matrix
matrix = in_matrix.create_matrix(int(input("Number of elements")))
summ_x = np.sum(matrix,axis = 1)
summ_y = np.sum(matrix, axis = 0)
min_x = np.min(summ_x)
max_x = np.max(summ_x)
min_y = np.min(summ_y)
max_y = np.max(summ_y)
if (max_x == min_x) and (max_x == max_y) and (max_y == min_y):
    print("Magic Square")
else:
    print("Not Magic Square")
