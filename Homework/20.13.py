#!/usr/bin/python3.5
# Sorry for documentaion
# But i can`t doc this
#
#
#
import numpy as np
import point_array_input as pai
import max_distanse as dist
import matplotlib as mpl
if __name__ == '__main__':
        n = int(input("Number of points"))
        distance_array = []
        for i in range(0,n):
                distance_array.append([])
        points = pai.input_point(n)
        k = 0
        for i in points:
                print(dist.distance(i,points))
                for j in dist.distance(i,points):
                        distance_array[k].append(j)
                k+=1
        distance_array = np.array(distance_array)
        max_dis = np.max(distance_array)
        index_pair_of_points = (None,None)
        for i in range(0,n):
                for j in range(0,n):
                           if(max_dis == distance_array[i][j]):
                                 index_pair_of_points = (i,j)                             
        print(distance_array)
        print(max_dis,' ',index_pair_of_points)

        
