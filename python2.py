#!/bin/python3

#import math
import matplotlib.pyplot as plt
import random
x=[]
y=[]

for n in range(1000):
    xrand=random.randrange(1,101)
    x.append(xrand)
    yrand=random.randrange(1,101)
    y.append(yrand)

plt.scatter(x,y)
plt.show()
