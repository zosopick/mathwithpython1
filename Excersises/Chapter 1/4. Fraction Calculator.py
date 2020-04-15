'''
Chapter 1
     Task 4
               Fraction Calculator

Create a program which can upon desire, add, subtract, divide or multiply two fractions
'''


from fractions import Fraction

def add(a,b):
     print('The result of adding {0} to {1} is {2}.'.format(a,b,a+b))

def subtract(a,b):
     print('The result of subtracting {0} from {1} is {2}.'.format(b,a,a-b))

def divide(a,b):
     print('The result of dividing {0} by {1} is {2}.'.format(a,b,a/b))

def multiply(a,b):
     print('The result of multiplying {0} with  {1} is {2}.'.format(a,b,a*b))
     
     


if __name__=='__main__':
     try:
          
          a=Fraction(input('Please enter the first fraction in the x/y form: '))
          b=Fraction(input('Please enter the second fraction in the x/y form: '))
          op=input('Please select one of the following operations to preform - Add, Subtract, Divide, Multiply: ')
     
          if op=='Add':
               add(a,b)

          if op=='Subtract':
               subtract(a,b)
          if op=='Divide':
               divide(a,b)
          if op=='Multiply':
               multiply(a,b)
     except ValueError:
          print('Invalid fraction entered.')
