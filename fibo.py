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
