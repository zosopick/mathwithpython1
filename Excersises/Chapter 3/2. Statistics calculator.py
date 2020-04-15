'''
Implement a statistics calculator that takes a list of numbers in the file mydata.txt and calculates and prints
their mean, median, mode, variance and standard deviation.
'''
#Taking the numbers out of the file
def read_data(filename):
     numbers=[]
     with open(filename) as f:
          for line in f:
               numbers.append(float(line))
          return numbers
     
#Calculating mean
def calculate_mean(numbers):
     s=sum(numbers)
     N=len(numbers)
     mean=s/N
     
#Calculating median
def calculate_median(numbers):
     N=len(numbers)
     numbers.sort()



     if N%2==0:
          m1=N/2
          m2=(N/2)+1

          m1=int(m1)-1
          m2=int(m2)-1
          median=(numbers[m1]+numbers[m2])

     else:
          m=(N+1)/2
          m=int(m)-1
          median=numbers[m]

     return median

#Calculating mode

from collections import Counter

def calculate_mode(numbers):
     c=Counter(numbers)
     mode=c.most_common(1)
     return mode [0][0]

#Calculating variance

     #We already have the mean so we won;t have to calculate it again
def calculate_mean(numbers):
     s=sum(numbers)
     N=len(numbers)
     mean=s/N

     return mean

def find_differences(numbers):
     mean=calculate_mean(numbers)
     diff=[]

     for num in numbers:
          diff.append(float(num - mean))
     return  diff

def calculate_variance(numbers):

     diff=find_differences(numbers)
     squared_diff=[]
     for d in diff:
          squared_diff.append(d**2)

     sum_squared_diff=sum(squared_diff)
     variance=sum_squared_diff/len(numbers)
     return variance






if __name__=='__main__':

     data=read_data('mydata.txt.txt')
     mean=calculate_mean(data)
     median=calculate_median(data)
     mode=calculate_mode(data)
     variance=calculate_variance(data)
     std=variance**0.5


     print('Mean: {0} '.format(mean))
     print('Median: {0}'.format(median))
     print('Mode: {0}'.format(mode))
     print('Variance: {0} '.format(variance))
     print('Standard deviation: {0}'.format(std))
