'''
Improve the function so that it first checks the length of the lists. Iff they are eqaul it may proceed,
otherwise it prints an error message
'''
def find_corr_x_y(x,y):
     if len(x)!=len(y):
          print('The two sets are of unequal size.')
          
     n=len(x)

     prod=[]
     for xi, yi in zip(x,y):
          prod.append((xi,yi))

     sum_prod_x_y=sum(x,y)
     sum_x=sum(x)
     sum_y=sum(y)
     squared_sum_x=sum_x**2
     squared_sum_y=sum_y**2

     x_square=[]
     for xi in x:
          x_square.append(xi**2)

     x_square_sum=sum(x_square)

     y_square=[]
     for yi in y:
          y_square.append(yi**2)

     y_square_sum=sum(y_square)

     numerator=n*sum_prod_x_y-sum_x*sum_y
     denominator_term1=n*x_square_sum-squared_sum_x
     denominator_term2=n*y_square_sum-squared_sum_y
     demoniator=(denominator_term1*denominator_term2)**2

     correlation=numerator/denominator


     return correlation
