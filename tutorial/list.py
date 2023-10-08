names = ['A', 'B', 'C', 'D','W']
print(names[1])
print(names[-2])
print(names[1:])
print(names[0:3])

#--------------------------------------------#

num = [2,4,5,43,65,54]

# first method
max_num = num[0]
for N in num:
    if N>max_num:
        max_num = N
print(max_num)

print(  )

#  Second method
print(max(num)) 
