'''
Chapter 7: Solving Calculus Problems
'''
#Finding the limit of a function

>>> from sympy import Limit, Symbol, S
>>> x=Symbol('x')
>>> Limit(1/x,x,S.Infinity)
Limit(1/x, x, oo, dir='-')


          #We must initialize it

>>> l=Limit(1/x,x,S.Infinity)
>>> l.doit()
0

          #We can choose from which side the limit comes
>>> Limit(1/x,x,0,dir='-').doit()
-oo

>>> Limit(1/x,x,0,dir='+').doit()
oo

          #The limit can also csolve limits of indeterminante forms (0/0)

>>> Limit(sin(x)/x,x,0).doit()
1

     #Continuous Comund interest
               #The compound interest is calculated as follows (p- principal amount, r- rate of interest ,t-number of years, n- number of compundings)
>>> from sympy import Symbol
>>> p=Symbol('p',positive=True)
>>> r=Symbol('r',positive=True)
>>> t=Symbol('t',positive=True)
>>> n=Symbol('n')
>>> from sympy import pprint
>>> A=p*(1+r/n)**(n*t)
>>> A
p*(1 + r/n)**(n*t)
     


               #If we let n go to Infinity, for it is continuous we get

>>> from sympy import Symbol, Limit, S
>>> p=Symbol('p',positive=True)
>>> r=Symbol('r',positive=True)
>>> t=Symbol('t',positive=True)
>>> n=Symbol('n')
>>> Limit(p*(1+r/n)**(n*t),n,S.Infinity).doit()
p*exp(r*t)


#Finding the Derivative of Functions

>>> from sympy import Symbol, Derivative
>>> t=Symbol('t')
>>> St=5*t**2+2*t+8
>>> Derivative(St,t).doit()
10*t + 2

     #We can substitute it for any value
>>> t1=Symbol('t1')
>>> d.doit().subs({t:t1})
10*t1 + 2
>>> d.doit().subs({t:1})
12

     #A derivative Calculator (which also does partial derivatives)

from sympy import Symbol, Derivative, sympify, pprint
from sympy.core import SympifyError

def derivative(f,var):
     var=Symbol(var)
     d=Derivative(f,var).doit()
     pprint(d)

if __name__=='__main__':
     f=input('Enter a functions: ')
     var=input('Enter the variable to differentiate with respect to: ')
     try:
          f=sympify(f)
     except SympifyError:
          print('Invalid input!')
     else:
          derivative(f,var)



#Higher-Order Derivates and Finding the Maxima and Minima


>>> from sympy import Symbol, solve, Derivative
>>> x=Symbol('x')
>>> f=x**5-30*x**3+50*x
>>> d1=Derivative(f,x).doit()

          #To find extrema we must solve f'(x)=0
>>> critical_points=solve(d1)
>>> critical_points
[-sqrt(9 - sqrt(71)), sqrt(9 - sqrt(71)), -sqrt(sqrt(71) + 9), sqrt(sqrt(71) + 9)]

          #They correspond to the points B,C,A,D

>>> A=critical_points[2]
>>> B=critical_points[0]
>>> C=critical_points[1]
>>> D=critical_points[3]

          #Now we find the value of f''(x) by substituting the value of each critical point.
          #If  f''(x) is less than 0 we have a maximum, if it's greated than 0 we have a minimum

>>> d2=Derivative(f,x,2).doit()
>>> d2.subs({x:B}).evalf()
127.661060789073
>>> d2.subs({x:C}).evalf()
-127.661060789073
>>> d2.subs({x:A}).evalf()
-703.493179468151
>>> d2.subs({x:D}).evalf()
703.493179468151

          #Points A and C are maxima and B and D are minima

>>> x_min=-5
>>> x_max=5
>>> f.subs({x:A}).evalf()
705.959460380365
>>> f.subs({x:C}).evalf()
25.0846626340294
>>> f.subs({x:x_min}).evalf()
375.000000000000
>>> f.subs({x:x_max}).evalf()
-375.000000000000

          #Point A seems to be a global maximum

>>> f.subs({x:B}).evalf()
-25.0846626340294
>>> f.subs({x:D}).evalf()
-705.959460380365
>>> f.subs({x:x_min}).evalf()
375.000000000000
>>> f.subs({x:x_max}).evalf()
-375.000000000000

               #Point D seems to be a global  minimum


#Finding the Global Maximum Using Gradiend Ascent

          #Use gradient ascent to find the angle at which the projectile
         # has maximum range for a fixed velocity, 25 m/s

import math
from sympy import Derivative, Symbol, sin

def grad_ascent(x0, f1x, x):
    epsilon =  1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

def find_max_theta(R, theta):
    # Calculate the first derivative
    R1theta = Derivative(R, theta).doit()
    theta0 = 1e-3
    theta_max = grad_ascent(theta0, R1theta, theta) 
    return theta_max

if __name__ == '__main__':
    g = 9.8
    # Assume initial velocity
    u = 25
    # Expression for range
    theta = Symbol('theta')
    R = u**2*sin(2*theta)/g
    theta_max = find_max_theta(R, theta)
    print('Theta: {0}'.format(math.degrees(theta_max)))
    print('Maximum Range: {0}'.format(R.subs({theta:theta_max})))


          #Use gradient  ascent to find the maximum value
          #of a single variable function

from sympy import Derivative, Symbol, sympify
from sympy.core import SympifyError

def grad_ascent(x0, f1x, x):
    epsilon =  1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

if __name__=='__main__':
     f=input('Enter a function with one variable: ')
     var=input('Enter the variable to differentiate with respect to: ')
     var0=float(input('Enter the initial value of the variable: '))

     try:
          f=sympify(f)
     except SympifyError:
          print('Invalid Input!!!')
     else:
          var=Symbol(var)
          d=Derivative(f,var).doit()
          var_max=grad_ascent(var0,d,var)
          print('{0}:   {1}'.format(var.name,var_max))
          print('Maximum value: {0}'.format(f.subs({var:var_max})))
          


               #Use gradient ascent to find the maximum value of a
               #single variable function. This also checks for the existence
               #of a solution for the equation f'(x)=0
          
from sympy import Derivative, Symbol, sympify, solve

def grad_ascent(x0,f1x,x):
     if not solve(f1x):
          print('Cannot continue, solution for {0}=0 does not exist'.format(f1x))
     epsilon=1e-6
     step_size=1e-4
     x_old=x0
     x_new=x_old+step_size*f1x.subs({x:x_old}).evalf()
     while abs(x_old-x_new)>epsilon:
          x_old=x_new
          x_new=x_old+step_size*f1x.subs({x:x_old}).evalf()

     return x_new

if __name__=='__main__':
     f=input('Enter a function with one variable: ')
     var=input('Enter the variable to differentiate with respect to: ')
     var0=float(input('Enter the initial value of the variable: '))
     try:
          f=sympify(f)
     except SympifyError:
          print('Invalid Function Entered')
     else:
          var=Symbol(var)
          d=Derivative(f,var).doit()
          var_max=grad_ascent(var0,d,var)
          print('{0}: {1}'.format(var.name,var_max))
          print('Maximum value: {0}'.format(f.subs({var:var_max})))




#Finding the Integrals of Functions

               #indefinite
>>> from sympy import Integral
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> k=Symbol('k')
>>> Integral(k*x,x)
Integral(k*x, x)
>>> Integral(k*x,x).doit()
k*x**2/2

>>> Integral(k*x,(x,0,2)).doit()
2*k


               #Definite

>>> from sympy import Integral, Symbol
>>> x=Symbol('x')
>>> Integral(x,(x,2,4)).doit()
6


#Probability Density Function (((-expr(x-center)**2)/2)/sqrt(2*math.pi)))

>>> from sympy import Symbol, exp, sqrt, pi, Integral
>>> x=Symbol('x')
>>> p=exp(-(x-10)**2/2)/sqrt(2*pi)
>>> Integral(p,(x,11,12)).doit().evalf()
0.135905121983278


     #With the probability Density functions, the proability from -Infinity to +Infinity must be 1


>>> from sympy import Symbol, pi, exp, sqrt, Integral, S
>>> x=Symbol('x')
>>> p=exp(-(x-10)**2/2)/sqrt(2*pi)
>>> Integral(p,(x,S.NegativeInfinity,S.Infinity)).doit().evalf()
1.00000000000000
