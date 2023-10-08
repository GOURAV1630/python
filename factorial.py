#### Factorial of a number
import math
def factorial(num):
    try:
        factorial = math.factorial(int(num))
        print(f'\nFactorial of number {num} is {factorial}\n')

    except ValueError:
        print( 'Invalid input. Enter a valid number.' )
    
    except Exception as e:
        print(e)
#################################
num =input('Enter number = ')
factorial(num) ###calling function factorial 