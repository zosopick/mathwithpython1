'''
Create a code which makes a graph out of 10 x input points and the y=x**2+2*x+1 function
'''

from pylab import plot,show,xlabel,ylabel
x_values=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y_values=[]

for x in x_values:
 
     y=x**2+2*x+1
     y_values.append(y)

plot(x_values,y_values)
xlabel('x values')
ylabel('y values')

show()

