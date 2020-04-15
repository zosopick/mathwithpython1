'''
In this challenge we have to write a program that will plot on a graph the relationship betwen consecutive Fibonacci numbers, for 100 numbers
'''
import matplotlib.pyplot as plt

def fibo(n):
     if n==1:
          return[1]
     if n==2:
          return[1,1]
     # For the case n>2
     a=1
     b=1
     #The first two numbers of a series
     series=[a,b]
     for i in range(n):
          c=a+b
          series.append(c)
          a=b
          b=c
     return series

def plot_ratio(series):
     ratios=[]
     for i in range(len(series)-1):
          ratios.append(series[i+1]/series[i])
     plt.plot(ratios)
     plt.title('Ratios between Fibonacci numbers & golden ratio')
     plt.ylabel('Ratio')
     plt.xlabel('Number')

     plt.show()
     

if __name__=='__main__':
     
     num=100

     series=fibo(num)
     plot_ratio(series)
