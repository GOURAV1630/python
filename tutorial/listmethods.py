num = [3,4,99,5,6,11,78,2,11]
num.append(234)
print(num)

num.insert(1,11)
print(num)

num.remove(78)
print(num)

num.pop()
print(num)

n=num.index(11)
print(n)

print(123 in num)
print(11 in num)

print(num.count(11))

num.sort()
print(num)
num.reverse()
print(num)

numbers = [2,2,4,6,3,4,6,1]
uniques = []

for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)

###_-------------------=------------===+++++++++++++++++++++++
##TUPLES
N = (1,2,4)
print(N[1])

