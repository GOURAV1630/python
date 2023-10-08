has_good_credit = False
has_good_income = True

if has_good_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

print(' ')

if has_good_credit or has_good_income:
    print("Eligible for loan")

print(' ')

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print("not eligible for loan")
