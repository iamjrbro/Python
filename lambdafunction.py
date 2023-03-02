'''
LAMBDA

Lambda it's a small function, without a name, that can and it's most communly used inside an other function or associated to an variable.
    1. it can have multiples arguments, but only one expression.
    2. it's mostly used to let the code more clean.
'''

# One argument
 
add = lambda x: x + 20
print(add(6))


# Multiples arguments
 
add = lambda w, x, y, z: w + x + y + z + 20
print(add(8, 6, 2, 4))


# Lambda inside another function
 
def add(x):
    func2 = lambda x: x + 60
    return func2(x) * 4

print(add(2))    