''''
Chapter 3
     Describing data with statistics.
               In this chapter we'll use python to desribe and beter undestands sets of data. After looking at some basic
          statistical measures - the mean, median mode and range- we'll move on to some more advanced measures
          such as variance and standard deviation. Calculating correlation coefficients will allow us to quantify the
          relationship between two sets of data. In the end we will talk about scatter plots.
'''

#Finding the Mean
     #sum() and len() fiunctions are of use to us

>>> shortlist=[1,2,3]
>>> sum(shortlist)
6

>>> len(shortlist)
3

     #Calculating the mean

def calculate_mean(numbers):
     s=sum(numbers)
     N=len(numbers)
     mean=s/N

     return mean

if __name__=='__main__':
     donations=[100,60,70,900,100,200,500,500,503,600,1000,1200]
     mean=calculate_mean(donations)
     N=len(donations)
     print('Mean donation over the last {0} days is {1}.'.format(N,mean))

#FINDING THE MEDIAN

     #We will use the sort() function.

>>> samplelist=[4,1,3]
>>> samplelist.sort()
>>> samplelist
[1, 3, 4]

     #Calculating the median

def calculate_median(numbers):
     N=len(numbers)
     numbers.sort()

     if N%2==0:
          m1=N/2
          m2=(N/2)+1

          m1=int(m1)-1
          m2=int(m2)-1
          median=(numbers[m1]+numbers[m2])/2

     else:
          m=(N+1)/2
          m=int(m)-1
          median=numbers[m]
     return median

if __name__=='__main__':
     donations=[100,60,70,900,100,200,500,500,503,600,1000,1200]
     medium=calculate_median(donations)
     N=len(donations)
     print('The median donation over the last {0} days is {1}.'.format(N,medium))
     

#Finding the mode and creating a frequency table

     #Finding the most common elements

>>> simplelist=[4,2,1,3,4]
>>> from collections import Counter
>>> c=Counter(simplelist)
>>> c.most_common()
[(4, 2), (2, 1), (1, 1), (3, 1)]


          #We can find the most common member  and see how many times it appears in the list
>>> c.most_common(1)
[(4, 2)]

          #We can extract him like this
>>> mode=c.most_common(1)
>>> mode[0]
(4, 2)
>>> mode[0][0]
4

     #Finding the mode

from collections import Counter

def calculate_mode(numbers):
     c=Counter(numbers)
     mode=c.most_common(1)
     return mode [0][0]

if __name__=='__main__':
     scores=[7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
     mode=calculate_mode(scores)

     print('The mode of this list of numbers is {0}.'.format(mode))



          #It can occur that a certain list has more than one mode. We handle it like this

from collections import Counter

def calculate_modes(numbers):
     c=Counter(numbers)
     numbers_freq=c.most_common()
     max_count=numbers_freq[0][1]

     modes=[]
     for num in numbers_freq:
          if num[1]==max_count:
               modes.append(num[0])
     return modes


if __name__=='__main__':
     scores=[5,5,5,4,4,4,9,1,3]
     modes=calculate_modes(scores)
     print('The modes(s) of the list of numbers are: ')
     for mode in modes:
          print(mode)


     #Getting a frequency table

from collections import Counter

def frequency_table(numbers):
     table=Counter(numbers)
     print('Number\tFrequency')
     for number in table.most_common():
          print('{0}\t{1}'.format(number[0],number[1]))

if __name__=='__main__':
     scores=[7,8,9,2,10,9,9,9,9,4,5,6,1,5,9,7,8,6,1,10]
     frequency_table(scores)



          #We can also sort it according to the numbers

from collections import Counter

def frequency_table(numbers):
     table=Counter(numbers)
     numbers_freq=table.most_common()
     numbers_freq.sort()

     print('Number \t Frequency')
     for number in numbers_freq:
          print('{0} \t {1}'.format(number[0],number[1]))

if __name__=='__main__':
     scores=[7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]
     frequency_table(scores)


#Measuring the dispersion

     #Finding the range of a set of numbers

def find_range(numbers):

     lowest=min(numbers)
     highest=max(numbers)
     r=highest-lowest

     return lowest,highest,r

if __name__=='__main__':
          donations=[100,60,70,900,100,200,500,500,503,600,1000,1200]
          lowest,highest,r=find_range(donations)
          print("Lowest: {1}    Highest: {1}    Range: {2}  ".format(lowest,highest,r))

     

     #Finding the Variance and standard deviation

def calculate_mean(numbers):
     s=sum(numbers)
     N=len(numbers)
     mean=s/N

     return mean

def find_differences(numbers):
     mean=calculate_mean(numbers)
     diff=[]

     for num in numbers:
          diff.append(num-mean)
     return diff

def calculate_variance(numbers):

     diff=find_differences(numbers)
     squared_diff=[]
     for d in diff:
          squared_diff.append(d**2)

     sum_squared_diff=sum(squared_diff)
     variance=sum_squared_diff/len(numbers)
     return variance

if __name__=='__main__':
     donations=[100,60,70,900,100,200,500,500,503,600,1000,1200]
     variance=calculate_variance(donations)
     print('The variance of the list of numbers is {0}.'.format(variance))

     std=variance**0.5
     print('The Standard deviation of the list is {0}.'.format(std))
     
     

#Calculating the correlation between two data sets

     #We can present two lists for a nice overview using the zip() function:

>>> simple_list1=[1,2,3]
>>> simple_list2=[2,4,6]
>>> for x,y in zip(simple_list1,simple_list2):
	print(x,y)

	
1 2
2 4
3 6

     #We can write a program to find the linear correlation between two coefficients for us:

def find_corr_x_y(x,y):
     n=len(x)

     prod=[]
     for xi, yi in zip(x,y):
          prod.append(xi,yi)

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

if __name


    #Reading data from a text file

def sum_data(filename):

     s=0
     with open(filename) as f:
          for line in f:
               s=s+float(line)
     print('The sum of numbers is {0}'.format(s))

if __name__=='__main__':
     sum_data('mydata.txt.txt')



     #Calculatig the mean of numbers stored in a file

def read_data(filename):

     numbers=[]
     with open(filename) as f:
          for line in f:
               numbers.append(float(line))

     return numbers


def calculate_mean(numbers):
     s=sum(numbers)
     N=len(numbers)
     mean=s/N

     return mean


if __name__=='__main__':
     data=read_data('mydata.txt.txt')
     mean=calculate_mean(data)

     print('The mean of the list is {0}'.format(mean))


     #Reading data from a .csv file

import csv
from matplotlib import pyplot as plt

def scatter_plot(x,y):
     plt.scatter(x,y)
     plt.xlabel('Numbers')
     plt.ylabel('Square')
     plt.show()

def read_csv(filename):

     numbers=[]
     squared=[]
     with open(filename) as f:
          reader=csv.reader(f)
          next(reader)
          for row in reader:
               numbers.append(int(row[0]))
               squared.append(int(row[1]))
          return numbers,squared

if __name__=='__main__':
     numbers,squared=read_csv('numbers.csv')
     scatter_plot(numbers,squared)






