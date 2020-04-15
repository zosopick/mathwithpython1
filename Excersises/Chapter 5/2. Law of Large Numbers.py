'''
The expectation, E, of a discrete random variable is the equivelent of the average
or mean that we learned about in chapter 3.

P(x=1) is that the probability that a fair n-sided die will roll a 1

The expecation can be calculated as follows:

          E=x1P(x1)+x2P(x2)+x3P(x3)+x4P(x4)+...+xnP(xn)

For a six-sided die it looks like this:

>>> e=1*(1/6)+2*(1/6)+3*(1/6)+4*(1/6)+5*(1/6)+6*(1/6)
>>> e
3.5

Your challenge is to verify this law when rolling a six-sided die for the following number of trials:
100, 1000, 10000, 100000 and 500000
'''

import random

def die_roll(num_trials):
     rolls=[]
     for t in range(num_trials):
          rolls.append(random.randint(1,6))
     return sum(rolls)/num_trials

if __name__=='__main__':
     e=3.5
     print('Expectation value: {0}.'.format(e))

     for trial in [100,1000,10000,100000,500000]:
          avg=die_roll(trial)
          print('Trials: {0}   Average: {1}'.format(trial,avg))


