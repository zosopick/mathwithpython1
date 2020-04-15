'''
The Henon functions transorms the point P(x,y) into Q(y+1-1.4x^2,0.3x)

Your challenge is to write a program to create a graph showing 20 000 iterations of this transformation.

Start at (1,1)

Also, Create an animatef figure  showing the points starting to lie along the curves!

'''

import matplotlib.pyplot as plt

def transform(p):
     x,y=p
     x1=y+1-1.4*x**2
     y1=0.3*x
     return x1,y1


if __name__=='__main__':
     p=(0,0)
     x=[p[0]]
     y=[p[1]]
     for i in range(20000):
          p=transform(p)
          x.append(p[0])
          y.append(p[1])


     plt.plot(x,y,'o')
     plt.show()
