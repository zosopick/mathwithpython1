

'''
Chapter 1: Working with numbers
'''

#Basic Mathematical Operations


  #Python can do simple mathematical operations (+-)

>>>>>>1+2
4.5

>>>1+3.5


>>>-1+2.5

>>>100-45

>>>-1.1+5

  #Multiplications also (*)

>>>3*2

>>>3.5*1.5

  #We can also divide using (/)

>>>3/2

>>>4/2

  #To get the result without any decimal values, we use the ''floor division'' operator (//)

>>>3//2

  #What is interesting about this is that it rounds down to the next lowest integer

>>>-3//2
-2

  #We can  also use the exponentional operator (**)

>>>2**2
4
>>>2**10
1024
>>>1**10
1

  #To find the n-th root we simply use the exponentional operator in the follwing manner
>>>8**(1/3)
2.0


  #Python uses the PEMDAS rules

>>>5+5*5
30

>>>(5+5)*5
50


#Labels: Attaching Names to Numbers

>>>a=3
>>>a+1
4

#Different kinds of numbers

  #Python can handle many different kinds of numbers

>>> type(3)
<class 'int'>

>>> type(3.5)
<class 'float'>

>>> type (3.0)
<class 'float'>

  #If we wish to get the integer part of a number we do it simply as follows

>>> int(3.8)
3

>>> int (3.0)
3

  #The function float() is similar, only it turns an integer number into a floating one


>>> float(3)
3.0


  #The standard Python package can also handle fractions

>>> from fractions import Fraction
>>> f=Fraction(3,4)
>>> f
Fraction(3, 4)

  #Python also allows us to combine different kinds of numbers in the same expression


>>> Fraction(3,4)+1+Fraction(1/4)
Fraction(2, 1)

  #Complex numbers can be made using the complex() function or by hand

>>> a=complex(2,3)
>>> a
(2+3j)
>>> b=3+3j
>>> b
(3+3j)
>>> a+b
(5+6j)
>>> a-b
(-1+0j)

>>> a*b
(-3+15j)
>>> a/b
(0.8333333333333334+0.16666666666666666j)

  #The modulus and floor division functions do not apply to complex numbers, however, we can find the real and imaginary parts of the number

>>> z=2+3j
>>> z.real
2.0
>>> z.imag
3.0

  #The conjugate can also be easily find using the conjugate() method

>>> z.conjugate()
(2-3j)

  #By using simple multiplication and exponentiation we can find the magnitude of a complex numbeer

>>> (z.real**2+z.imag**2)**(1/2)
3.605551275463989

  #Or by simply using the abs() function

>>> abs(z)
3.605551275463989


  #Getting user input

  #As our programs get more and more complicated it will be needed that certain
  #variables are input manually. We can do that like this:

>>> a=input()
1
>>> a
'1'


  #Python was developed to take strings into account. We mark them by eithger using '' or ""

>>> s1='a string'
>>> s2="a string"

  #If a string is made only of numbers, we can convert it to an integer or a float number

>>> int(a)+1
2
>>> float(a)+1
2.0

 #Fractions and Complex Numbers as Input
>>> a=Fraction(input('Enter a fraction: '))
Enter a fraction: 3/0
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a=Fraction(input('Enter a fraction: '))
  File "C:\ProgramData\Anaconda3\lib\fractions.py", line 178, in __new__
    raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
ZeroDivisionError: Fraction(3, 0)

  #If it encounters dividing by 0, we must write an exception for it

>>> try:
	a=Fraction(input('Enter the fraction: '))
except ZeroDivisionError:
	print('Invalid fraction')

	
Enter the fraction: 3/0

  #The complex() function can change a string into a complex number

>>> z=complex(input('Enter a complex number in the form a+jb: '))
Enter a complex number in the form a+jb: 2+3j
>>> z
(2+3j)

  #However, the number cannot be entered with spaces inbetween

>>> z=complex(input('Enter a complex number in the a+bj form: '))
Enter a complex number in the a+bj form: 2 + 3j
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    z=complex(input('Enter a complex number in the a+bj form: '))
ValueError: complex() arg is a malformed string


#Writing Programs that do the Math for You


  #Calculating the factors of an integer

>>> def is_factor(a,b):
    if b%a==0:
        return True
    else:
        return False

>>> is_factor(4,1024)
True

  #Introducing the range() function

>>> for i in range(1,4):
	print(i)

	
1
2
3

    #If we put a single element as input into range() it will start from 0

>>> for i in range(5):
	print(i)

	
0
1
2
3
4

    #We can adapt it by adding another argument so that it moves in steps of 2

>>> for i in range(1,10,2):
	print(i)

	
1
3
5
7
9


      #Here is a program on finding the factors of an integer


def factors(b):

    for i in range(1,b+1):
        if b%i==0:
            print(i)

if __name__=='__main__':

    b=input('Your Number Please: ')
    b=float(b)

    if b>0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')




  #Generating Multiplication Tables
>>> item1='apples'
>>> item2='bannanas'
>>> item3='grapes'

>>> print('At the grocery store, I bought some {0} and {1} and {2}.'.format(item1,item2,item3))
At the grocery store, I bought some apples and bannanas and grapes.


    #We do not need to preenter the members of fomat(). We can just do it on the go.

>>> print('Number 1: {}. Number 2: {}. Number 3: {}'.format(1,2.58826,3.1415926535))
Number 1: 1. Number 2: 2.58826. Number 3: 3.1415926535


    #And then our multiplication table looks like this:

def multi_table(a):

    for i in range(1,11):
        print('{0}x{1}={2}'.format(a,i,a*i))


if __name__=='__main__':
    a=input('Enter a number: ')
    multi_table(float(a))
              
    #The function .fomat() can be adapted to only take a certain number of decimal places

>>> '{0:.2f}'.format(1.234567)
'1.23'
>>> '{0:.2f}'.format(1)
'1.00'

  #Converting Units of Measurment

    #25.4 Inches to meters

>>> (25.4*2.54)/100
0.64516


    #650 Miles to kilometers

>>> 650*1.609
1045.85


    #98.6 Farrehnheit into degrees Celsius

>>> F=98.6
>>> (F-32)*(5/9)
37.0


    #37 Celsius into Farrenheit

>>> C*(9/5)+32
98.60000000000001


    #We can make a program for several conversions at once



def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km=float(input('Enter the distance in Kilometers: '))
    miles=km/1.609

    print('The above given distance is {0} miles.'.format(miles))

def miles_km():
    miles=float(input('Enter the distance in Miles: '))
    km=miles*1.609

    print('The above given distance is {0} kilometers.'.format(km))

if __name__=='__main__':
    print_menu()
    choice=input('Which Conversion would you like to do? ')
    if choice=='1':
        km_miles()
    if choice=='2':
        miles_km()


#Finding the Roots of a Quadratic Equation
        
def roots(a,b,c):

    D=(b*b-4*a*c)**0.5
    x_1=(-b+D)/(2*a)
    x_2=(-b-D)/(2*a)

    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if __name__=='__main__':
    
    
    a=input('Enter a: ')
    b=input('Enter b: ')
    c=input('Enter c: ')

    roots(float(a), float(b), float(c))








