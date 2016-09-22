#!/usr/bin/python3.5
import numpy as np
import numpy.random as rnd 
import matplotlib.pyplot as plt
import max_distanse
e = 0.0000000000000000000000001
n = int(input("Number of points"))
x = rnd.uniform(-1,1,n)
y = rnd.uniform(-1,1,n)
#print(x,y)

plt.xlabel("x")
plt.ylabel("y")
#plt.plot(x,y)
q = np.linspace(-1,1,100)
r = np.linspace(-1,-1,100)
plt.plot(q,r)
plt.plot(q,-r)
plt.plot(r,q)
plt.plot(-r,q)
w = np.sqrt(-q**2 + 1)
plt.plot(q,w)
plt.plot(q,-w)
z = zip(x,y)
z = list(z)
z = np.array(z)
#print(z)
zero = np.zeros(2)
dist = max_distanse.distance(z,zero)
print("dist.size-",dist.size)
number_in = dist[dist - 1.0 < e]
#print(number_in.__class__)
number_in = float(number_in.size)
print("number_in-",number_in)
pi = ((number_in)/n)*4
pi = str(pi)
print(pi)
plt.title("PI"+'-'+pi)
plt.scatter(x,y)
plt.show()




