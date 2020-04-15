'''
Wrte a program to find a desired percentile p of a given list of numbers

     1.  Order the list of numbers in an ascending order
     2. Calculate i==((n*p)/100)+0.5 where n is the number of items in the list, and p the percentile
     3. if i is an integer, data[i] will gives us the number corresponding the percenile p
     4. if i is not an integer, set k to the integer part of i and f to the fractional part of i
          the number (1-f)*data[k]+f*data[k+1]will give is the number at percentile p
'''


def find_percentile_score(data,p):
     if p <0 or p >100:
          return None
     data.sort()
     if p==0:
          return data[0]
     if p==100:
          return data[-1]

     n=len(data)
     i=((n*p)/100)+0.5

     if i.is_integer():
          real_idx=int(i-1)
          return data[real_idx]
     else:
          k=int(1)
          f=1-k
          real_idx_1=k-1
          real_idx_2=k
          return (1-f)*data[real_idx_1]+f*data[real_idx_2]

def read_data(filename):
     numbers=[]
     with open(filename) as f:
          for line in f:
               numbers.append(float(line))
          return numbers

if __name__=='__main__':
     p=float(input('Please enter the percentile you wish to calculate: '))
     data=read_data('marks.txt')
     percentile_score=find_percentile_score(data,p)
     if percentile_score:
          print('The score at {0} percentile is {1}'.format(p,percentile_score))
     else:
          print('Count not find the score corresponding to {0} percentile.'.format(p))
