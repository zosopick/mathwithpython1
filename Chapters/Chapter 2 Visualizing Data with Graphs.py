'''
Chapter 2: Visualising data with graphs
'''

#Working with Lists and Tuples

                #Lists can be used to hold numbers and we can extract the individual members
>>> simplelist=[1,2,3]
>>> simplelist[0]
1
>>> simplelist[1]
2
>>> simplelist[2]
3
>>>

                #They can also host strings

>>> stringlist=['string a','string b','string c']
>>> stringlist[0]
'string a'
>>> stringlist[1]
'string b'
>>> stringlist[2]
'string c'


                #The best thing about this is that we can make empty lists and then add members later on in the code

>>> emptylist=[]
>>> emptylist
[]
>>> emptylist.append(1)
>>> emptylist
[1]
>>> emptylist.append(2)
>>> emptylist
[1, 2]


                #Tuples are akin to lists. Instead of square brackets we use parentheses

>>> simpletuple=(1,2,3)
>>> simpletuple[1]
2
>>> simpletuple[0]
1
>>> simpletuple[2]
3


        #Iterating over a List or Tuple
>>> l=[1,2,3]
>>> for item in l:
	print(item)

	
1
2
3


                #We can also use the enumerate() function to see which member is in which place

>>> l=(1,2,3)
>>> for index,item in enumerate(l):
	print(index,item)

	
0 1
1 2
2 3


        #Creating Graphs with Matplotlib

x_numbers=[1,2,3]
y_numbers=[2,4,6]
from pylab import plot,show
plot(x_numbers,y_numbers)
show()


        #Marking Points on the Graph by adding the marker='o' ; * x + can be used instead

x_numbers=[1,2,3]
y_numbers=[2,4,6]
from pylab import plot,show
plot(x_numbers,y_numbers,marker=o)
show()


        #Graphing the Average Annual Temperature in NYC

from pylab import plot,show

nyc_temp=[53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
plot(nyc_temp, marker='+')
show()

                #We can also add the years

from pylab import plot,show

nyc_temp=[53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
years=range(2000,2013)
plot(years,nyc_temp, marker='+')
show()


        #Comparing the Monthly Temperature trends of NYC; adding legend()

from pylab import plot,show,legend

nyc_temp_2000=[31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006=[40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012=[37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months=range(1,13)
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012,marker='o',)
legend([2000,2006,2012])

show()


        #Customizing graphs:

                #adding a title and labels

from pylab import plot,show,legend, title, xlabel, ylabel

nyc_temp_2000=[31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006=[40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012=[37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]

months=range(1,13)
plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012,marker='o',)
legend([2000,2006,2012])
title('Average monthly temperatures in NYC')
xlabel('Month')
ylabel('Temperature in degrees F')
show()


                #customizing the axes

from pylab import plot,show,axis

nyc_temp=[53.9,56.3,56.4,53.4,54.5,55.8,56.8,55.0,55.3,54.0,56.7,56.4,57.3]
plot(nyc_temp, marker='+')
axis(ymin=0)
show()


                #plotting using pyplot

import matplotlib.pyplot

def create_graph():
     x_numbers=[1,2,3]
     y_numbers=[2,4,6]

     matplotlib.pyplot.plot(x_numbers,y_numbers)
     matplotlib.pyplot.show()

if __name__=='__main__':
     create_graph()


                    #we can also shorten the name matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def create_graph():
     x_numbers=[1,2,3]
     y_numbers=[2,4,6]

     plt.plot(x_numbers,y_numbers)
     plt.show()

if __name__=='__main__':
     create_graph()


                #saving the plots using savefig

from pylab import plot,savefig
x=[1,2,3]
y=[2,4,6]
plot(x,y)
savefig('C:\mygraph.png')

#Plotting with Formulas

        #Newtons Law of Universal Gravity

'''
The relationship between gravitational force and the distance between two bodies
'''

import matplotlib.pyplot as plt

def draw_graph(x,y):
     #This draws the graph
     plt.plot(x,y,marker='o')
     plt.xlabel('Distance in meters')
     plt.ylabel('Gravitational force in Newtons')
     plt.title('Newtons law')
     plt.show()

def generate_F_r():
     #This generates values for r
     r=range(100,1001,50)
     #Empty list to store the calculated values of F
     F=[]
     #G, the constant
     G=6.674*(10**(-11))
     #The two masses
     m1=0.5
     m2=1.5

     for dist in r:
          force=(G*m1*m1)/(dist**2)
          F.append(force)

     #We need to call the draw_graph() function
     draw_graph(r,F)

if __name__=='__main__':
     generate_F_r()


        #Generating equally spaced floating point numbers

def frange(start,final,increment):
     numer=[]
     while start<final:
          numbers.append(start)
          start=start+increment

     return numbers


        #Drawing the Trajectory of a Projectile


from matplotlib import pyplot as plt
import math

def draw_graph(x,y):
     plt.plot(x,y)
     plt.xlabel('x-coordinate')
     plt.ylabel('y-coordinate')
     plt.title('Motion of a projectile ball')

def frange(start,final,interval):

     numbers=[]
     while start<final:
          numbers.append(start)
          start=start+interval

     return numbers

def draw_trajectory(u,theta):
     theta=math.radians(theta)
     g=9.81

     t_flight=2*u*math.sin(theta)/g
     intervals=frange(0,t_flight,0.001)
     x=[]
     y=[]
     for t in intervals:
          x.append(u*math.cos(theta)*t)
          y.append(u*math.sin(theta)*t-0.5*g*(t**2))
                   
     draw_graph(x,y)

if __name__=='__main__':
     try:
          u=float(input('Enter the initial velocity in m/s: '))
          theta=float(input('Enter the initial angle of projection in degrees: '))
     except ValueError:
          print('You entered an invalid input!')
     else:
          draw_trajectory(u,theta)
          plt.show()

                #Comparing the Trajectory at different initial velocities but the same theta



from matplotlib import pyplot as plt
import math

def draw_graph(x,y):
     plt.plot(x,y)
     plt.xlabel('x-coordinate')
     plt.ylabel('y-coordinate')
     plt.title('Motion of a projectile ball')

def frange(start,final,interval):

     numbers=[]
     while start<final:
          numbers.append(start)
          start=start+interval

     return numbers

def draw_trajectory(u,theta):
     theta=math.radians(theta)
     g=9.81

     t_flight=2*u*math.sin(theta)/g
     intervals=frange(0,t_flight,0.001)
     x=[]
     y=[]
     for t in intervals:
          x.append(u*math.cos(theta)*t)
          y.append(u*math.sin(theta)*t-0.5*g*(t**2))
                   
     draw_graph(x,y)

if __name__=='__main__':

     u_list=[20,40,60]
     theta=45
     for u in u_list:
         draw_trajectory(u,theta)

plt.legend(['20','40','60'])
plt.show()






