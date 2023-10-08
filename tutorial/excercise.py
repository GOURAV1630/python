Name = input('Enter your name ')

if len(Name)<3:
    print("Name must be atleast 3 characters")
elif len(Name)>50:
    print("Name must be a maximum of 50 characeters")

else:
    print("Name length is acceptable")