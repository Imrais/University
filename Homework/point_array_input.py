import numpy as np
def input_point(n):
	a = np.zeros((n, 2))
	for i in range(0,n):
		s = input()
		s = s.split()
		a[i][0] = float(s[0])
		a[i][1] = float(s[1])
	return a
if __name__ == '__main__':
	n = int(input())
	a = input_point(n)
	print(a)