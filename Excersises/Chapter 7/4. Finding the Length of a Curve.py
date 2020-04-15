'''
Write a program that calculates the length of an arc of a function from any point a to any point b
'''
from sympy import Symbol, Integral, sympify, Derivative,sqrt
from sympy.core import SympifyError


def derivative(function):
     x=Symbol('x')
     func=Derivative(function,x).doit()
     return func

def integrator(func,start,final):
     x=Symbol('x')
     f=sqrt(1+(func)**2)
     length=Integral(f,(x,start,final)).doit()
     return length

if __name__=='__main__':

     function=input('Please enter a desired funciton in terms of x: ')
     start=float(input('Please enter the start of the curve: '))
     final=float(input('Please enter the end of the curve: '))

     try:
          function=sympify(function)
     except SympifyError:
          print('Invalid Fuction!')
     else:
          func=derivative(function)
          length=integrator(func,start,final)

          print('The length of the desired curve is {0}'.format(length))
          pause

