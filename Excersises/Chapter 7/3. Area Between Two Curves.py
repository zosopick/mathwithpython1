'''

Your challenge is to write a program that will allow the user to input any two single-variable
functions of x and print the enclosed area between the two. The program should make it clear that
the first function entered should be the upper function and it should also asl for the values of
x between which to find the area
'''


from sympy import Symbol, Integral, sympify
from sympy.core import SympifyError

def integrator(ftop,fbot,start,final):
     x=Symbol('x')
     f=ftop-fbot
     area=Integral(f,(x,start,final)).doit()
     return area

if __name__=='__main__':
     ftop=input('Please enter the single-variable function in terms of x which is above: ')
     fbot=input('Please enter the single-variable function in terms of x which is below: ')
     start=float(input('Please enter the left bound of the integral: '))
     final=float(input('Please enter the right bound of the integral: '))

     try:
          ftop=sympify(ftop)
          fbot=sympify(fbot)
     except SympifyError:
          print('At least one of the functions entered was invalid! Please run the program anew and enter a proper function!')
     else:
          area=integrator(ftop,fbot,start,final)
          print('The area between {0} and {1}, between the values {2} and {3} is {4}.'.format(ftop,fbot,start,final,area))
          
