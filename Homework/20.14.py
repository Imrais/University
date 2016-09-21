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
e = 0.00001
if __name__ == '__main__':
        n = int(input("Number of points"))
        distance_array = []
        for i in range(0,n):
                distance_array.append([])
        points = pai.input_point(n)
        k = 0
        for i in points:
                #print(dist.distance(i,points))
                for j in dist.distance(i,points):
                        distance_array[k].append(j)
                k+=1
        distance_array = np.array(distance_array)
        point_triple = np.zeros((n,n,n))
        max_triple = [0,0,0]
        for i in range(0,n):
            for j in  range(0,n):
                for c in range(0,n):
                    if(i == j):
                        continue
                    if(j == c):
                        continue
                    if(c == i):
                        continue
                    if((distance_array[i][j] - distance_array[i][c] -  distance_array[c][j])>e):
                        continue
                    if((distance_array[i][c] - distance_array[c][j] - distance_array[i][j])>e):
                        continue
                    if((distance_array[c][j] - distance_array[i][c] - distance_array[i][j])>e):
                        continue
                    #print(i,' ',j,' ',c)
                    point_triple[i][j][c] = distance_array[i][j] + distance_array[i][c] + distance_array[c][j]
                    if (point_triple[i][j][c] > point_triple[max_triple[0]][max_triple[1]][max_triple[2]]):
                        max_triple[0] = i
                        max_triple[1] = j
                        max_triple[2] = c
        print(max_triple)
        if (max_triple == [0,0,0]):
            print("No triangle here")
        else:
            print('Indexes of points which have max perimeter',max_triple[0],' ',max_triple[1],' ',max_triple[2])

