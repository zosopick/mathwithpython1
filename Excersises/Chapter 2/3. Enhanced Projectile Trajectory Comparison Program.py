from matplotlib import pyplot as plt
import math
g=9.81

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

def draw_trajectory(u,theta,t_flight):
     theta=math.radians(theta)
     

     t_flight=2*u*math.sin(theta)/g
     intervals=frange(0,t_flight,0.001)
     x=[]
     y=[]
     for t in intervals:
          x.append(u*math.cos(theta)*t)
          y.append(u*math.sin(theta)*t-0.5*g*(t**2))
                   
     draw_graph(x,y)


if __name__=='__main__':
     num_trajectories=int(input('How many trajectories would you like to plot at the same time? '))
     velocities=[]
     angles=[]
     for i in range(1,num_trajectories+1):
          v=input('Enter the initial velocity for trajectory {0} in (m/s): '.format(i))
          theta=input('Enter the initial launch angle for the trajectory {0} in degrees: '.format(i))
          velocities.append(float(v))
          angles.append(math.radians(float(theta)))

     for i in range(num_trajectories):
          t_flight=2*velocities[i]*math.sin(angles[i])/g
          S_x=velocities[i]*math.cos(angles[i])*t_flight
          S_y=velocities[i]*math.sin(angles[i])*(t_flight/2)-(1/2)*g*(t_flight*2)**2
          print('Initial velocity: {0}, Angle of projection: {1} .'.format(velocities[i],math.degrees(angles[i])))
          print('T_flight: {0:.3f} s, x_max: {1:.3f} m, y_max: {2:.3f} m.'.format(t_flight,S_x,abs(S_y)))
          print()
          draw_trajectory(velocities[i],angles[i],t_flight)
     legends=[]
     for i in range(0,num_trajectories):
          legends.append('{0} m/s   -   {1} degrees'.format(velocities[i],math.degrees(angles[i])))
     plt.legend(legends)
     plt.show()
