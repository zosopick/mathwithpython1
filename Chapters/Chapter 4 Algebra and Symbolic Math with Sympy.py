'''
Chapter 4: Algebra and Symbolic Math with sympy
'''

#Defining symbols and symbolic operations


     #For any Symbol object, its name attrirubte is a string that is actally the symbol it represemts
>>> x=Symbol('x')
>>> x+x+1
2*x + 1


>>> a=Symbol('x')
>>> a+a+1
2*x + 1

     #For any Symbol object, its name attrirubte is a string that is actally the symbol it represemts

>>> x=Symbol('x')
>>> x.name
'x'

>>> a=Symbol('x')
>>> a.name
'x'


     #We import the symbols like this

>>> from sympy import symbols
>>> x,y,z=symbols('x,y,z')
>>> s=x*y+x*y
>>> s
2*x*y



#Working with expressions

     #Factorizing and expanding expressions

>>> from sympy import Symbol
>>> x=Symbol('x')
>>> y=Symbol('y')
>>> from sympy import factor
>>> expr=x**2+y**2
>>> factor(expr)
x**2 + y**2
>>> expr=x**2-y**2
>>> factor(expr)
(x - y)*(x + y)

>>> from sympy import expand
>>> factors=factor(expr)
>>> expand(factors)
x**2 - y**2


>>> from sympy import factor,expand
>>> expr=x**3+3*x*y**2+3*y*x**2+y**3
>>> factors=factor(expr)
>>> factors
(x + y)**3
>>> expand(factors)
x**3 + 3*x**2*y + 3*x*y**2 + y**3

     #Pretty printing

>>> from sympy import pprint
>>> expr
x**3 + 3*x**2*y + 3*x*y**2 + y**3
>>> pprint(expr)
 3      2          2    3
x  + 3*x *y + 3*x*y  + y


>>> expr=1+2*x+2*x**2
>>> pprint(expr)
   2          
2*x  + 2*x + 1


     #Since this orders them so the highest power comes first, we can reverse it using the init_printing
     # and setting order='rev-lex'. (Doesn;t work)

>>> from sympy import init_printing
>>> init_printing(order='rev-lex')
>>> pprint(expr)
   2          
2*x  + 2*x + 1



     #Printing a series

from sympy import Symbol,pprint, init_printing

def print_series(n):

     init_printing(order='rev-lex')

     x=Symbol('x')
     series=x
     for i in range(2,n+1):
          series=series+(x**i)/i
     pprint(series)

if __name__=='__main__':
     n=input('Enter the number of terms you want in the series: ')
     print_series(int(n))


     #Substituting values using the expr.subs({}) function

>>> from sympy import symbols
>>> x,y=symbols('x,y')
>>> x*x+x*y+x*y+y*y
 2            2
y  + 2*x*y + x 
>>> expr=x*x+x*y+x*y+y*y
>>> res=expr.subs({x:1,y:2})
>>> res
9

>>> expr.subs({x:1-y})
       2                  2
(1 - y)  + 2*y*(1 - y) + y 


>>> expr_subs=expr.subs({x:1-y})
>>> from sympy import simplify
>>> simplify(expr_subs)
1

     #Python can also host custom made dictionaries. THese data structures containg key-valued pairs inside
     #curly braces. We use it as follows

>>> sampledict={'1st':'A','2nd':'B','3rd':'C'}
>>> sampledict['1st']
A

     #Calculating the value of a list

     

from sympy import Symbol, pprint, init_printing

def print_series(n,x_value):

     x=Symbol('x')
     series=x
     for i in range(2,n+1):
          series=series+(x**i)/i

     pprint(series)

     series_value=series.subs({x:x_value})
     print('Value of the series at {0} is {1:.2f}'.format(x_value,series_value))

if __name__=='__main__':
     x_value=input('Enter the value of x at which you wish to evaluate the series: ')
     n=input('Enter the number of terms you want in the series: ')

     print_series(int(n),float(x_value))


     #Converting Strings to Mathematical Expressions

>>> from sympy import sympify
>>> expr=input('Enter a mathematical expression: ')
Enter a mathematical expression: x**2+3*x+x**3+2*x
>>> expr=sympify(expr)
>>> 2*expr
2*x**3 + 2*x**2 + 10*x


     #In the case of an invalid input it ought to give us an error

>>> from sympy import sympify
>>> from sympy.core.sympify import SympifyError
>>> expr=input('Enter a mathematical expression: ')
Enter a mathematical expression: x**2+3*x+x**3+2x
>>> try:
	expr=sympify(expr)
except SympifyError:
	print('Invalid Input')

Invalid Input


     #We can also write a program which allows the sympify() function calculate the product of two expressions

from sympy import expand,sympify
from sympy.core.sympify import SympifyError

def product(expr1,expr2):
     prod=expand(expr1*expr2)
     print(prod)

if __name__=='__main__':
     expr1=input('Please enter the first expression: ')
     expr2=input('Please enter the second expression: ')

     try:
          expr1=sympify(expr1)
          expr2=sympify(expr2)

     except SympifyError:
          print('Invalid input!')

     else:
          product(expr1,expr2)


#Solving equations

     #Linear

>>> from sympy import Symbol, solve
>>> x=Symbol('x')
>>> expr=x-5-7
>>> solve(expr)
[12

     #Quadratic

 >>> from sympy import Symbol, solve
>>> x=Symbol('x')
>>> expr=x**2+5*x+4
>>> solve(expr,dict=True)
[{x: -4}, {x: -1}]q

 >>> from sympy import Symbol,solve
>>> x=Symbol('x')
>>> expr=x**2+x+1
>>> solve(expr,dict=True)
[{x: -1/2 - sqrt(3)*I/2}, {x: -1/2 + sqrt(3)*I/2}]
>>>


      #Solving for One Variable in Terms of Others

 >>> from sympy import symbols, solve
>>> x,a,b,c=symbols('x,a,b,c')
>>> expr=a*x*x+b*x+c
>>> solve(expr,x,dict=True)
[{x: (-b + sqrt(-4*a*c + b**2))/(2*a)}, {x: -(b + sqrt(-4*a*c + b**2))/(2*a)}]
     


>>> from sympy import symbols,solve,pprint
>>> s,u,t,a=symbols('s,u,t,a')
>>> expr=u*t+(1/2)*a*t*t-s
>>> t_expr=solve(expr,t,dict=True)
>>> pprint(t_expr)
             ______________        /       ______________\   
            /            2         |      /            2 |   
     -u + \/  2.0*a*s + u         -\u + \/  2.0*a*s + u  /   
[{t: ----------------------}, {t: -------------------------}]
               a                              a              
>>> print(t_expr)
[{t: (-u + sqrt(2.0*a*s + u**2))/a}, {t: -(u + sqrt(2.0*a*s + u**2))/a}]





      #Solving a System of Linear Equations

 >>> from sympy import symbols, solve
>>> x,y=symbols('x,y')
>>> exprq=2*x+3*y-6
>>> expr2=3*x+2*y-12
 >>> solve((exprq,expr2),dict=True)
[{x: 24/5, y: -6/5}]

      #Checking the solution:

 >>> soln=solve((exprq,expr2),dict=True)
>>> soln=soln[0]
>>> exprq.subs({x:soln[x],y:soln[y]})
0
>>> expr2.subs({x:soln[x],y:soln[y]})
0


 #Plotting using sympy

 >>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> plot(2*x+3)


      #If we dont want x from -10 to 10 as is standard but from -5 to 5 we do this

 >>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> plot((2*x+3),(x,-5,5))

      #We can further decorate the plot

 >>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> plot((2*x+3),(x,-5,5),title='A line',xlabel='x',ylabel='2x+3')

      #We can also save it if we please


>>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
 >>> p=plot((2*x+3),(x,-5,5),title='A fancy plot',ylabel='2x+3',xlabel='x')
 >>> p.save('A fancy plot.png')


      #Plotting expressions input by the user (doesnt work)

 from sympy import symbols,solve,sympify
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def plot_expression(expr):
     y=symbols('y')
     solutions=solve(expr,y)
     expr_y=solutions[0]
     plot(expr_y)

if __name__=='__main__':
     expr=input('Please enter your expression in terms of x and y: ')

     try:
          expr=sympify(expr)
     except SympifyError:
          print('Invalid Input!')
     else:
          plot_expression(expr)


     #Plotting multiple functions onto single graph

>>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> plot(2*x+3,3*x+1)

     #We can adapt the colors of the graphs so we can differentiate them

>>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> p=plot(2*x+3,3*x+1, legend=True,show=False)
>>> p[0].line_color='b'
>>> p[1].line_color='r'
>>> p.show()


