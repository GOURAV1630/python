N = int(input('Enter your number:- '))
order = len(str(N))
temp = N
sum = 0

while temp>0:
    r = temp % 10
    sum = sum + (r**order)
    temp = temp//10

if N == sum:
    print('Number is ARMSTRONG NO.')
else:
    print('number is not ARMSTRONG NO.')

