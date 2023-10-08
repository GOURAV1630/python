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
            print(f'\nOne or both nums are odd. Hence SUM is:-  {sum}\n')
        
    except Exception as e:
        print(e)

cal_sum_or_expo()


# using Lambda fucntion
a=int(input('Enter 1st num:-  '))
b=int(input('Enter 2nd number:- '))

result= lambda a , b: (a%2==0 and b%2==0)  and f'Both are even. Exponent is {(a**b)}'or f'One of the no. is odd. Sum is {(a+b)}'

print(f'\n{result(a,b)}')
