class Mammal:
    def walk(self):
        print('Loyal pet')
        print('Feed them well')

    def run(self):
        print('Run')


class Dog(Mammal):
    pass 


class Cat(Mammal):
    def annoying(self):
        print("""
Cats are not good 
and are Annoying
        """)


dog1 = Dog()
dog1.walk()

print(' ')

a = Cat()
a.annoying()
