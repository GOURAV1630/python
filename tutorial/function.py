def greet_user(first,second):
    print(f'Hi {first} and {second}!')
    print('Welcome aboard')

print("Start")
greet_user('Gourav','Rishika')
print('Finish')

## Keyword argument
greet_user(second= 'asdf', first='QWERTY')

## when assigning keyword argument , note that keyword argument
## can only be assigned after positional argument
