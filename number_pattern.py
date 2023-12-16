n = int(input('Enter number:- '))
for i in range(n):
    for j in range(i+1):
        print('1',end=" ")
    print()

###-------------------------------------------------------------
#Right triangle
n = int(input('Enter number:- '))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()

###----------------------------------------------------------
#Left triangle
n = int(input('Enter number:- '))
p=1
for i in range(n):
    for k in range(i+1):
        print(' ',end=" ")
    for j in range(n-i):
        print(p,end=" ")
    p+=1
    print()
##-------------------------------------------------------
# Hill pattern
n = int(input('Enter number:- '))
p=1
for i in range(n):
    for j in range(n-i):
        print(' ',end=" ")
    for I in range(i+1):
        print(p,end=" ")
    for k in range(i):
        print(p,end=" ")
    p+=1
    print()
##----------------------------------------------------------
# Reverse Hill pattern
n = int(input('Enter number:- '))
p=1
for i in range(n):
    for j in range(i+1):
        print(' ',end=" ")
    for I in range(n-i):
        print(p,end=" ")
    for k in range((n-1)-i):
        print(p,end=" ")
    p+=1
    print()
##-------------------------------------------------------
# Decrementing rows
n = int(input('Enter number:- '))
p=n
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print() 
#-----------------------------------------------------------
#rows