#!/usr/bin/python3.5
import numpy as np
import point_array_input as pai
def distance(single_point,points):
	dist = (points - single_point) ** 2
	dist = np.sum(dist, axis=1)
	dist = np.sqrt(dist)
	return dist
if  __name__ == '__main__':
	single_point = [3, 4]
	points = pai.input_point(int(input("Number of points")))
	print(points)
	dist_arr = distance(single_point,points)
	print(dist_arr)
