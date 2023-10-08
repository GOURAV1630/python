customer = {
    "name": "GOURAV",
    'surname':'GUPTA',
    "age" : 22,
    "verified": True
}

print (customer["name"])
print(customer['surname'])

print(customer.get('Rollno','001'))
customer["name"] = "Rishika"
print(customer["name"])
