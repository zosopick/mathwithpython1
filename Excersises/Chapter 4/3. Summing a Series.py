'''
Create a program which is capable of finding a sum of an arbitrary series when you supply the n-th term
of the series and the number of terms in it
'''
from sympy import symbols, summation, pprint, sympify

def find_sum(nth_term,num_terms):
     n=symbols('n')
     s=summation(nth_term,(n,1,num_terms))
     pprint(s)

if __name__=='__main__':
     nth=sympify(input('Please enter the n-th term of the series: '))
     num=int(input('Please enter the number of terms in the series: '))

     find_sum(nth,num)
     

