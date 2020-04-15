

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
    while True:
        try:
            num=float(input('Enter an integer: '))
            if num.is_integer():
                even_odd(num)
            else:
                print('Please enter an integer: ')
        
        except ValueError:
            print('Please enter a number')

        answer=input('Would you like to exit? (y) for yes. ')
        if answer=='y':break
 
            
