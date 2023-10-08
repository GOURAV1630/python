
## --- SQUARE PATTERN

n = int(input('enter your number ='))
for i in range(n):
    for I in range(n):
        print('@ ' , end = ' ')
    print()

##----INCREASING Triangle

n = int(input('enter your number ='))
for i in range(n):
    for I in range(i+1):
        print('@ ' , end = ' ')
    print()

##-----DECREASING Triangle
n = int(input('enter your number ='))
for i in range(n):
    for I in range(i, n):
        print('@ ',end = ' ')
    print()

##----RIGHT SIDED Triangle
n = int(input('enter your number ='))
for i in range(n):
    for I in range(i,n):
        print(' ', end = ' ')
    for I in range(i+1):
        print('@' , end = ' ')
    print()

##---Right sided triangle upside-down
n = int(input('enter your number ='))
for i in range(n):
    for I in range(i+1):
        print(' ' , end = ' ')
    for j in range(i,n):
        print('*',end = ' ')
    print()

##---HILL Pattern 
n = int(input('enter your number ='))
for i in range(n):
    for I in range(i,n):
        print(' ', end = ' ')
    for I in range(i+1):
        print('@' , end = ' ')
    for j in range(i):
        print('@', end = ' ')
    print()

##--Reverse hill pattern
n = int(input('Enter number = '))

for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n):
        print('*',end=" ")
    for I in range(i,n-1):
        print('*', end=' ')
    print()

##---DIAMOND pattern
n = int(input('enter your number ='))
for i in range(n-1):
    for I in range(i,n):
        print(' ', end = ' ')
    for I in range(i+1):
        print('*' , end = ' ')
    for j in range(i):
        print('*', end = ' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,n):
        print('*',end=" ")
    for I in range(i,n-1):
        print('*', end=' ')
    print()

