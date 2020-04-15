'''
Chapter 1
     Task 5
          Give Exit Power to the user

Write a multiplication table which offers the user an choice whether to show the multuplication tablr for another number or to quit the program
'''
'''
Here is an example on how to create a loop using while True and break
def fun():
     print('I am an endles loop')

if __name__=='__main__':
     while True:
          fun()
          answer=input('Do you want to exit? (y) for yes. ')
          if answer =='y':
               break
'''

def multi_table(a):

    for i in range(1,11):
        print('{0}x{1}={2}'.format(a,i,a*i))


if __name__=='__main__':
     while True:
         a=input('Enter a number: ')
         multi_table(float(a))

         answer=input('Would you like to exit? (y) for yes. ')
         if answer=='y':
               break
              
