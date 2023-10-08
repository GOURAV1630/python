def outer_func(x):
    def inner(y):
        return x + y
    return inner

result = outer_func(5)

print(result)
