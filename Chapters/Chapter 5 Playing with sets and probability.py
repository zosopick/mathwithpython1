'''

Chapter 5: Playing with sets and probability

'''


#What is a Set

     #Set construction
>>> from sympy import FiniteSet
>>> s=FiniteSet(1,2,3)
>>> s
{1, 2, 3}

          #A set can also hold any value

>>> from sympy import FiniteSet
>>> from fractions import Fraction
>>> s=FiniteSet(1,1.5,Fraction(2,5))
>>> s
{2/5, 1, 1.5}


          #The cardinality of a set is the number of members in the set. We can find it using len()

>>> s=FiniteSet(1,1.5,3)
>>> len(s)
3


          #Checking whetehr a number is in a set

>>> s=FiniteSet(1,2,3,5)
>>> 4 in s
False


          #Creating an empty set

>>> s=FiniteSet()
>>> s
EmptySet()


          #Creating a set from Lists or Tuples

>>> members=[1,2,3,4,5]
>>> s=FiniteSet(*members)
>>> s
{1, 2, 3, 4, 5}

          #Set Repetition and order

>>> from sympy import FiniteSet
>>> members=[1,2,3,2]
>>> FiniteSet(*members)
{1, 2, 3}


               #Two sets are said to be equal when they have the same mebers, irrelevant of their order

>>> s=FiniteSet(3,4,5)
>>> t=FiniteSet(5,4,3)
>>> s==t
True


          #Subsets,Supersets and Power Sets

               #A set s is a subset of another set t  if all the members of s are also members of t

>>> s=FiniteSet(1)
>>> t=FiniteSet(1,2)
>>> s.is_subset(t)
True
>>> t.is_subset(s)
False

               #An empty set is also a susbset of every set.
               #Also, any set is a subset of itself


>>> e=FiniteSet()
>>> e.is_subset(t)
True
>>> e.is_subset(s)
True
>>> s.is_subset(s)
True
>>> t.is_subset(t)
True

               #A set t is a superset of another set s, if t contains all of the members contained in s.

>>> s.is_superset(t)
False
>>> t.is_superset(s)
True

               #The power set of a set,s, is the set of all possible subsets of s. Any set has exactly
               #2^(cardinality) subsets. i.e. The set {1,2,3} has excatcly 8 since 2^3=8


>>> s=FiniteSet(1,2,3)
>>> ps=s.powerset()
>>> ps
{EmptySet(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
>>> len(ps)
8


               #A set s is a proper subset of t iff t contains all the members of s and at least one more member.
               #A set t is a proper superset of s iff t contains all the members of s and at least one more member.

>>> s=FiniteSet(1,2,3)
>>> t=FiniteSet(1,2,3)
>>> s.is_proper_subset(t)
False
>>> t.is_proper_superset(s)
False

>>> t=FiniteSet(1,2,3,4)
>>> s.is_proper_subset(t)
True
>>> t.is_proper_superset(s)
True

         #Set Operations

               #Union and intersection

>>> s=FiniteSet(1,2,3)
>>> t=FiniteSet(2,4,6)
>>> s.union(t)
{1, 2, 3, 4, 6}

>>> s=FiniteSet(1,2)
>>> t=FiniteSet(2,3)
>>> s.intersect(t)
{2}

                    #We can make an union and intersection of more than 2 sets

>>> s=FiniteSet(1,2,3)
>>> t=FiniteSet(2,4,6)
>>> u=FiniteSet(3,5,7)
>>> s.union(t).union(u)
{1, 2, 3, 4, 5, 6, 7}

>>> s.intersect(t).intersect(u)
EmptySet()


          #Cartesian product

>>> from sympy import FiniteSet
>>> s=FiniteSet(1,2)
>>> t=FiniteSet(3,4)
>>> p=s*t
>>> p
{1, 2} x {3, 4}


>>> for elem in p:
	print(elem)	
(1, 3)
(1, 4)
(2, 3)
(2, 4)

               #The cardinality of the Cartesian Product is the product of the cardinality of the sets

>>> len(p)==len(s)*len(t)
True

               #If we apply the expnential operator to a set, we get the Cartesian product of that set
               # times itself the specified number of times.

>>> from sympy import FiniteSet
>>> s=FiniteSet(1,2)
>>> p=s**3
>>> p
{1, 2} x {1, 2} x {1, 2}
>>> for elem in p:
	print(elem)

(1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 2, 2)
(2, 1, 1)
(2, 1, 2)
(2, 2, 1)
(2, 2, 2)


          #Applying a Formula to Multiple Sets of Variables

               #Check the formula for the values of 15,18, 21, 22.5 and 25

from sympy import FiniteSet,pi

def time_period(length):
     g=9.8
     T=2*pi*(length/g)**0.5
     return T

if __name__=='__main__':
     L=FiniteSet(15,18,21,22.5,25)
     for l in L:
          t=time_period(l/100)
          print('Length: {0} cm   Time Perdiod: {1:.3f} s'.format(float(l),float(t)))


               #The output for which is

Length: 15.0 cm   Time Perdiod: 0.777 s
Length: 18.0 cm   Time Perdiod: 0.852 s
Length: 21.0 cm   Time Perdiod: 0.920 s
Length: 22.5 cm   Time Perdiod: 0.952 s
Length: 25.0 cm   Time Perdiod: 1.004 s


               #Different Gravity, Different Results (9.8, 9.78, 9.83)

from sympy import FiniteSet, pi

def time_period(length,g):
     T=2*pi*(length/g)**0.5
     return T

if __name__=='__main__':

     L=FiniteSet(15,18,21,22.5,25)
     g_values=FiniteSet(9.8,9.78)

     print('{0:^15}{1:^15}{2:^15}'.format('Lentgh(cm)','Gravity(m/s^2)','Time Period(s)'))

     for elem in L*g_values:
          l=elem[0]
          g=elem[1]
          t=time_period(l/100,g)

          print('{0:^15}{1:^15}          {2:^15.3f}'.format(float(l),float(g),float(t)))

                    #For which the output is

            Lentgh(cm)   Gravity(m/s^2) Time Period(s) 
     15.0           9.78                     0.778     
     15.0            9.8                     0.777     
     18.0           9.78                     0.852     
     18.0            9.8                     0.852     
     21.0           9.78                     0.921     
     21.0            9.8                     0.920     
     22.5           9.78                     0.953     
     22.5            9.8                     0.952     
     25.0           9.78                     1.005     
     25.0            9.8                     1.004




#Probability

          #Experiment is simply the test we want to perform. A Trial is a single run of the experiment.

          #Sample space is the set of all possible outcomes. For a six sided die it's {1,2,3,4,5,6}.

          #Event is a set of outcomes we want to calculate. It forms a subset of the sample space.

          #If there is a uniform distribution, the probability  of an event P(E) is calculated by:

def probability(space,event):
     return len(event)/len(space)


          #Finding the probability of a prime number wappearing when a 20-sided die is rolled

from sympy import FiniteSet

def probability(space,event):
     return len(event)/len(space)

                    #Here we take an integer and check whether it's divisible with no remainder by any number
                    #between 2 and itself

def check_prime(number):
     if number !=1:
          for factor in range(2,number):
               if number%factor==0:
                    return False

     else:
          return False
     return True

if __name__=='__main__':
     space=FiniteSet(*range(1,21))
     primes=[]
     for num in space:
          if check_prime(num):
               primes.append(num)
     event=FiniteSet(*primes)
     p=probability(space,event)

print('Sample space: {0}'.format(space))
print('Event: {0}'.format(event))
print('Probability of rolling a prime: {0:.5f}'.format(p))


               #There was an easier way of creating this without the sets

from sympy import FiniteSet

def probability(space,event):
     return len(event)/len(space)

                    #Here we take an integer and check whether it's divisible with no remainder by any number
                    #between 2 and itself

def check_prime(number):
     if number !=1:
          for factor in range(2,number):
               if number%factor==0:
                    return False

     else:
          return False
     return True

if __name__=='__main__':
     space=range(1,21)
     primes=[]
     for num in space:
          if check_prime(num):
               primes.append(num)
     p=probability(space,primes)

print('Sample space: {0}'.format(space))
print('Event: {0}'.format(primes))
print('Probability of rolling a prime: {0:.5f}'.format(p))


          #Probability of Event A or Event B


               #In the set S={1,2,3,4,5}, the probability that a number is odd or a prime represents
               # the probability of union of the two sets: {1,3,5}U{1,3,5}={1,2,3,5}

               
>>> from sympy import FiniteSet
>>> s=FiniteSet(1,2,3,4,5,6)
>>> a=FiniteSet(2,3,5)
>>> b=FiniteSet(1,3,5)
>>> e=a.union(b)
>>> len(e)/len(s)
0.6666666666666666

          #Probability of Event A and Event B

               #For the same set as above, the  proability that a number is odd and a prime is represented
               #by the probability of an intersection of the two sets:

>>> from sympy import FiniteSet
>>> s=FiniteSet(1,2,3,4,5,6)
>>> a=FiniteSet(2,3,5)
>>> b=FiniteSet(1,3,5)
>>> e=a.intersect(b)
>>> len(e)/len(s)
0.3333333333333333


          #Generating Random Numbers

               #Simulating a Die Roll (random.randint(x,y) gives a random integer between x and y, inclusive



>>> import random
>>> random.randint(1,6)
2
>>> random.randint(1,6)
2
>>> random.randint(1,6)
5

          #Can you roll that score

               #We roll a six sided die until we've roled a total of 20

import matplotlib.pyplot as plt
import random

target_score=20

def roll():
     return random.randint(1,6)

if __name__=='__main__':
     score=0
     num_rolls=0
     while score<target_score:
          die_roll=roll()
          num_rolls+=1
          print('Rolled: {0}'.format(die_roll))
          score+=die_roll

     print('Score of {0} is reached in {1} rolls.'.format(score,num_rolls))

               #It gives an output:
Rolled: 2
Rolled: 3
Rolled: 2
Rolled: 5
Rolled: 1
Rolled: 2
Rolled: 6
Score of 21 is reached in 7 rolls.


               #Is the Target Score Possible?

from sympy import FiniteSet
import random

def find_prob(target_score,max_rolls):
     die_sides=FiniteSet(*range(1,7))

     s=die_sides**max_rolls

     if max_rolls>1:
          success_rolls=[]
          for elem in s:
               if sum(elem)>=target_score:
                    success_rolls.append(elem)
     else:
          if target_score>6:
               success_roll=[]
          else:
               success_rolls=[]
               for roll in die_sides:
                    if roll>=target_score:
                         success_rolls.append(roll)
     e=FiniteSet(*success_rolls)

     return len(e)/len(s)

if __name__=='__main__':

     target_score=int(input('Enter the targert score: '))
     max_rolls=int(input('Enter the maximum number of rolls allowed: '))

     p=find_prob(target_score,max_rolls)
     print('Probability: {0:.5f}'.format(p))

               #Output

Enter the targert score: 7
Enter the maximum number of rolls allowed: 2
Probability: 0.58333


          #Nonuniform Random Numbers

               #Let's say we have a nonuniform coin that has the probability of 2/3 to get heads
               #and 1/3 to get tails

import random

def toss():
     #0-> Heads, 1-> Tails

     if random.random()<2/3:
          return 0
     else:
          return 1

               #A virtual ATM that dispenses dollar bills of various denominations with varying probability:

import random

def get_index(probability):
     c_probability=0
     sum_probability=[]
     for p in probability:
          c_probability+=p
          sum_probability.append(c_probability)
     r=random.random()
     for index, sp in enumerate(c_probability):
          if r<sp:
               return index
     return len(probability)-1
def dispense():

     dollar_bills=[5,10,20,50]
     probability=[1/6,1/6,1/3,2/3]
     bill_index=get_index(probability)
     return dollar_bills[bill_index]

     

