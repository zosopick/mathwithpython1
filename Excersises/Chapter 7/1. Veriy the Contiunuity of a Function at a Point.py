'''
Your rask is to write a program which will
1 accept a single variable function and a value of that variable as inputs and
2 check whether the input funciton is continouus at the point where the variable assumes the input.

'''
from sympy import Symbol, Limit, sympify
from sympy.core import SympifyError

def limes(function,variable,point):
     x=Symbol('x')
     
     lim1=Limit(function,variable,point,dir='-').doit()

     lim2=Limit(function,variable,point,dir='+').doit()

     return lim1,lim2
def checker(lim1,lim2):
     if lim1==lim2:
          print('The function {0} is continuous at {1}.'.format(function,point))
     else:
          print('The function {0} is not continuous at {1}.'.format(function, point))

if __name__=='__main__':
     function=input('Enter a function with one variable: ')
     variable=input('Enter the variable: ')
     point=float(input('Enter the point to check the continuity at: '))

     try:
          function=sympify(function)
     except SympifyError:
          print('Invalid input!')
     else:
         lim1,lim2=limes(function,variable,point)
         checker(lim1,lim2)
     
     
