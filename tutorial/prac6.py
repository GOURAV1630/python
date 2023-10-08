import random


for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['A' , 'D', 'B', 'QWERTY', 'HARRY']
print(random.choice(members))
