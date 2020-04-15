'''
Chapter 1
     Task 2
               Enhanced Unit Calculator

               Write a program which can convert kilometers to miles, vice versa; kilograms to pounds and vice versa; Celsius to Fahrehnheit, vice versa;


 '''
def print_menu():
     print('1.Kilometers to Miles.')
     print('2. Miles to Kilometers.')
     print('3. Kilograms to Pounds.')
     print('4. Pounds to Kilograms.')
     print('5. Degrees Celsius to degrees Fahrenheit.')
     print('6. Degrees Fahrenheit to degrees Celsius.')

def km_miles():
     km=float(input('Please enter the distance in Kilometers: '))
     miles=km/1.609

     print('The above given distance is {0} Miles.'.format(miles))

def miles_km():
     miles=float(input('Please enter the distance in Miles: '))
     km=miles*1.609

     print('The above given distance is {0} Kilometers.'.format(km))

def kg_pounds():
     kg=float(input('Please enter the desired mass in Kilograms: '))
     pounds=kg*2.204

     print('The above given mass is {0} pounds.'.format(pounds))

def pounds_kg():
     pounds=float(input('Please enter the desired mass in Pounds: '))
     kg=pounds/2.204

     print('The above given mass is {0} Kilograms.'.format(kg))

def c_f():
     c=float(input('Please enter the desired temperature in degrees Celsius: '))
     f=c*(9/5)+32

     print('The above given temperature is {0} degrees Fahrenheit.'.format(f))

def f_c():
     f=float(input('Please enter the desired temperature in degrees Fahrenheit: '))
     c=(f-32)*(5/9)

     print('The above given temperature value is {0} fegrees Celsius.'.format(c))

if __name__=='__main__':
     print_menu()
     choice=input('Which conversion would you like? ')
     
     if choice=='1':
          km_miles()
          
     if choice=='2':
          miles_km()
          
     if choice=='3':
          kg_pounds()
          
     if choice=='4':
           pounds_kg()
           
     if choice=='5':
           c_f()
           
     if choice=='6':
           f_c()
           
                                                                 
