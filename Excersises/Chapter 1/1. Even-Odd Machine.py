'''
Even-odd vending machine.

1. Print whether the number is even or odd

2. Display the number followed by the next 9 evens or odds

use is_integer() to display an error if a non integer is given!


'''

def even_odd(num):

    if num%2==0:
        print('The number is even.')
    else:
        print('The number is odd.')
    count=1
    while count <=9:
        num +=2
        print(num)
        count +=1


if __name__=='__main__':
    try:
        num=float(input('Enter an integer: '))
        if num.is_integer():
            even_odd(num)
        else:
            print('Please enter an integer: ')
    except ValueError:
        print('Please enter a number')
