# Decrementing rows
n = int(input('Enter number:- '))
p=n
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print()