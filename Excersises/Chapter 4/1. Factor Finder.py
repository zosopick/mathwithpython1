'''
Make a program which asks the user to input an expression, calculates its factors and prints them
It ought to handle invalid input by making use of exception handling
'''
from sympy import symbols,factor,sympify
from sympy.core.sympify import SympifyError



def factorizer(expr):
      x,y=symbols('x,y')
      factorized=factor(expr)
      return factorized


if __name__=='__main__':
     expr1=input('Please enter an expression to be factorized: ')
     
     try:
          expression=sympify(expr1)
     except SympifyError:
          print('The input is invalid and cannot be factorized.')
     else:
          factorizer(expression)
          print('The factor of {0} is'.format(expression))
          print('{0}'.format(factorizer(expression)))
