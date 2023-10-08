import math

weight = int(input('Enter your weight = '))
unit = input('Enter unit l(lb) or k(kg) = ')

if unit.upper() == 'L':
    weight_in_kilograms = weight * 0.45
    print(f'You are {math.ceil(weight_in_kilograms)} kilos ')

elif unit.upper() == 'K':
    weight_in_pounds = weight / 0.45
    print(f'You are {math.ceil(weight_in_pounds)} pounds')