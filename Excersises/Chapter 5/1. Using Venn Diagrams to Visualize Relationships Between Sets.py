'''
In this challenge you will use Venn Diagramms.

To get to know you with them we will first run a few trials.

Create a Venn diagram if the set of positive odd numbers less than 20 {1,3,5,7,9,11,13,15,17,19}
and the set of all prime numbers less than 20 {2,3,5,7,11,13,17,19}.

You can use the matplotlib_venn package

from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

def draw_venn(sets):

     venn2(subsets=sets)
     plt.show()

if __name__=='__main__':
     s1=FiniteSet(1,3,5,7,9,11,13,15,17,19)
     s2=FiniteSet(2,3,5,7,11,13,17,19)

     draw_venn([s1,s2])
     

We can also decorate it by adding
venn2(subsets=(a,b),set_labels=('S','T'))

For your challenge imagine you've created an online questionare asking your classmates:
     Do you play football, another sport, or no sports?
Once ypu have the results create a CSV file, sports.csv as follow:

StudentID, Footbal, Others
1,1,0
2,1,1
3,0,1
--snip--

Create 20 such rows for the 20 students in your class. Write a program to create a Venn diagram
to depict the sumarized results of the survey.

Dpending on the data in sports.cvv the numbers in each set will vary/.
The following function reads a CSV file and returns two lists corresponding to the IDs of the
students who play football and other sports.

def read_csv(filename):
     football=[]
     others=[]
     with open(filename) as f:
          reader=csv.reader(f)
          next(reader)
          for row in reader:
               if row[1]=='1':
                    football.append(row[0])
               if row[2]=='2':
                    others.append(row[0])

     return football, others

'''
import csv
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet


def read_csv(filename):
     football=[]
     others=[]
     with open(filename) as f:
          reader=csv.reader(f)
          next(reader)
          for row in reader:
               if row[1]=='1':
                    football.append(row[0])
               if row[2]=='1':
                    others.append(row[0])
     return football,others



def draw_venn(f,o):
     venn2(subsets=(f,o),set_labels=('Playing football','Playing other sports'))
     plt.show()

if __name__=='__main__':
     football,others=read_csv('sports.csv')
     foot=FiniteSet(*football)
     othe=FiniteSet(*others)
     draw_venn(foot,othe)

