import time
##definig this decorator at the beginning so that in every program can be used to calculate start and end time
def decorator(func):   
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print(f'\nStart time: {start_time:.2f}')
        func(*args, **kwargs)
        end_time = time.time()
        print(f'\nEnd time: {end_time:.2f}')
        execution_time = end_time - start_time
        print(f"Execution time: { execution_time:.2f} seconds")
    return wrapper
#--------------------------------------
#### Factorial of a number
import math

@decorator
def factorial(num):
    try:
        factorial = math.factorial(int(num))
        print(f'\nFactorial of number {num} is {factorial}\n')

    except ValueError:
        print( 'Invalid input. Enter a valid number.' )
    
    except Exception as e:
        print(e)

num =input('Enter number = ')
factorial(num) ###calling function factorial 
#----------------------------------------------------------------------------------------------------

### Fibonaccie Series
@decorator
def fibonacci(num):
        n1,n2 = 0,1
        sum = 0
        if num<=0:
            print('Enter number greater than zero')
        else:
            for i in range(num):
                print(sum,end=' ')
                n1 = n2
                n2 = sum
                sum = n1 + n2
try:
    num = int(input('Enter number to get the fibonacci series: '))
    fibonacci(int(num))
except:
    print('Enter a valid number/non decimal number to get fibo. series.')
#---------------------------------------------------------------------------

## Temperature Conversion.
@decorator
def temperatue_Conversion():
    def cel_to_fah():
        C = float(input('Enter temperature in Celcius = '))
        F = (C * 9/5) + 32
        print(f'\n{C}°C is equal to {F}°F')

    def fah_to_Cel():
        F = float(input('Enter temperature in Fahrenheit = '))
        C = (F - 32) * 5/9
        print(f'\n{F}°F is equal to {C}°C')
    while True:
        print('\nOptions')
        print(' 1:- Convert Celcius to Fahrenheit')
        print(' 2:- Convert Fahrenheit to Celcius')
        print(' 3:- No thanks. \n')
        
        choice = int(input('Enter your choice(1,2 or 3).='))
        print(' ')
        if choice==1:
            cel_to_fah()
        elif choice ==2:
            fah_to_Cel()
        elif choice==3:
            break
        else:
            print('Enter valid choice.(1, 2 or 3). Try again')
            break

temperatue_Conversion()
#------------------------------------------------------------------------------
## Enter two num and Calculate sum or Exponent
@decorator
def cal_sum_or_expo():
    try:
        num = []
        for i in range(2):
            n = int(input(f'Enter num {i+1}= '))
            num.append(n)    
        c=0
        for i in num: ###checking for both numbers in the list are even or not
            if i%2 == 0:
                c = c+1
        # if c(count) is 2 the it will print exponent of numbers taken 
        # since both are even.
        #if c(count) is 1 or 0 means that one or both the numbers taken are odd
        # and returns the sum of two numbers in the list num=[]
        if c==2:
            exponent = pow(num[0],num[1])
            print(f'\nSince both numbers are even, exponent is:- {exponent}')
        elif c==1 or c==0:
            sum = num[0] + num[1]
            print(f'\nOne or both nums are odd. Hence SUM is:-  {sum}')
        
    except Exception as e:
        print(e)

cal_sum_or_expo()

#---------------------------------------------------
# using Lambda fucntion
a=int(input('Enter 1st num:-  '))
b=int(input('Enter 2nd number:- '))

result= lambda a , b: (a%2==0 and b%2==0)  and f'Both are even. Exponent is {(a**b)}'or f'One of the no. is odd. Sum is {(a+b)}'

print(f'\n{result(a,b)}')
##----------------------------------------------------

###  print even place Fruits
fruits = ['Apple','Mango','Orange','Cherry','Banana','kiwi','Lichi']
print(fruits[::2])

#Check Fruits name length is even or not
for value in fruits:
    if len(value) %2==0:
        print(value)

# using list comprehension
even = [value for value in fruits if len(value) %2==0]
print(even)