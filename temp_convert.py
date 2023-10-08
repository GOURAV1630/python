## Temperature Conversion

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
