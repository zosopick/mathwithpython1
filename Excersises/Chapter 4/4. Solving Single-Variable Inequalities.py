'''
sympy can also solve inequalities(<,> and so on)
For this challenge we will create a function isolve(), which takes any inequality, solves it,
and then returns the solution.
There are three types of inequalities: Polynomial, rational and other. We have to use the correct one
or we get an error.

To solve a polynomian one (i.e. -x**2+4<0) we use the solve_poly_inequality() function:

>>> from sympy import Poly, Symbol, solve_poly_inequality
>>> x=Symbol('x')
>>> ineq_obj=-x**2+4<0
>>> lhs=ineq_obj.lhs
>>> p=Poly(lhs,x)
>>> rel=ineq_obj.rel_op
>>> solve_poly_inequality(p,rel)
[Interval.open(-oo, -2), Interval.open(2, oo)]
>>> 


For rational inequalities (i.e. ((x-1)/(x+2))>0) we use the solve)_rational_inequalities function:

>>> from sympy import Symbol, Poly, solve_rational_inequalities
>>> x=Symbol('x')
>>> ineq_obj=((x-1)/(x+2))>0
>>> lhs=ineq_obj.lhs
>>> numer,denom=lhs.as_numer_denom()
>>> p1=Poly(numer)
>>> p2=Poly(denom)
>>> rel=ineq_obj.rel_op
>>> solve_rational_inequalities([[((p1,p2),rel)]])
Union(Interval.open(-oo, -2), Interval.open(1, oo))

For any other type (i/.r. sin(x)-0.6>0) we will use the solve_univariate_inequality() function:
)
>>> from sympy import Symbol, solve, solve_univariate_inequality, sin
>>> x=Symbol('x')
>>> ineq_obj=sin(x)-0.6>0
>>> solve_univariate_inequality(ineq_obj,x,relational=False)
Interval.open(0.643501108793284, -0.643501108793284 + pi)



It is also helpful to remember these handy functions:

     is_polynomial()
>>> x=Symbol('x')
>>> expr=x**2-4
>>> expr.is_polynomial()
True
>>> expr=2*sin(x)+3
>>> expr.is_polynomial()
False
>>>


     is_rational()

>>> expr.is_rational_function()
True
>>> expr=2+x
>>> expr.is_rational_function()
True
>>> expr=2+sin(x)
>>> expr.is_rational_function()
False



When you run your program it should ask the user to input an inequality expression and print back
the solution
'''

from sympy import Symbol,sympify, SympifyError
from sympy import solve_poly_inequality,solve_rational_inequalities
from sympy import solve_univariate_inequality, Poly
from sympy.core.relational import Relational, Equality

def poly_solver(ineq_obj):
     #This is a prequisite for every function
     x=Symbol('x')
     expr=ineq_obj.lhs
     rel=ineq_obj.rel_op
     
     #First we check if the function is polynomial and solve if it is
     
     if expr.is_polynomial():
          p=Poly(expr,x)
          return solve_poly_inequality(p,rel)

     #If the function is not polynomial we use elif(else if) to check whether it is rational, if so we solve

     elif expr.is_rational_function():
          numer,denom=expr.as_numer_denom()
          p1=Poly(numer)
          p2=Poly(denom)
          return solve_rational_inequalities([[((p1,p2),rel)]])

     #If it's none of the above we simply solve for other
     
     else:
          return solve_univariate_inequality(ineq_obj,x,relational=False)
     

if __name__=='__main__':
     ineq=input('Please enter an inequality: ')

     #We check for faulty input
     try:
          ineq_obj=sympify(ineq)
     except SympifyError:
          print('Invalid Inequality!')
     else:
          if isinstance(ineq_obj,Relational) and not isinstance(ineq_obj,Equality):
               print(poly_solver(ineq_obj))
          else:
               print('Invalid Inequality')
     


     
