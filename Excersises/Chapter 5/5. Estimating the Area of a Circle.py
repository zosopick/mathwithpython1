'''
Consider a square of the surface area A. Inside of it is an inscribed dartoard.

Now consider we throw some darts onto the square. the ones which hit the darboard are N
the ones which hit the outisde square are M. Total number of darts thrown is N+M


The percentage of darts which hit the dartbboard is f=N/(N+M). For a high enough number
of darts f*A is approximately are the area of the dartboard.


The first part of this challenge is writing a program which finds the estimate area of a circle of any
given radius using this approach. The program ough to give us results for 3 numbers of darts thrown:
10^3,10^5 and 10^6.

We will input our own radius and the program will do the calculations

'''

'''
First part

import math
import random

def estimate(radius,total_throws):
     center=(radius,radius)

     in_circle=0

     for i in range(total_throws):
          x=random.uniform(0,2*radius)
          y=random.uniform(0,2*radius)
          p=(x,y)
          d=math.sqrt((p[0]-center[0])**2+(p[1]-center[1])**2)
          if d<=radius:
               in_circle+=1
     area_of_square=(2*radius)**2
     return (in_circle/total_throws)*area_of_square

if __name__=='__main__':
     radius=float(input('Please enter the desired radius: '))
     area_of_circle=math.pi*radius**2
     for points in [10**3, 10**5, 10**6]:
          print('Area: {0}, Estimated ({1} throws): {2}'.format(area_of_circle,points,estimate(radius,points)))


'''

'''
The area of the square is 4*r**2 and the area of the circle inscribed is math.pi*r**2.
If we divide the area of the circle by the area of the square, we get math.pi/4

The function f from above is an approximation of math.pi/4 and thus:

4*(N/(N+M)) ought to be math.pi

Adapt the program from above so it calculates pi for the given number valus and any radius

'''
import math
import random

def calculate(radius,total_throws):
     center=(radius,radius)

     in_circle=0

     for i in range(total_throws):
          x=random.uniform(0,2*radius)
          y=random.uniform(0,2*radius)
          p=(x,y)
          d=math.sqrt((p[0]-center[0])**2+(p[1]-center[1])**2)
          if d<=radius:
               in_circle+=1
     return (in_circle/total_throws)*4

if __name__=='__main__':
     radius=1
    
     for points in [10**3, 10**5, 10**10]:
          print('Pi: {0}    Calculated Value for {1} throws: {2}'.format(math.pi,points,calculate(radius,points)))
                


