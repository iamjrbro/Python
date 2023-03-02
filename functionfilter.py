'''
FILTER FUNCTION

Used to apply a function to an iterable, per item (list, tuple, dictionary, etc.).
    -> it's generally, used with Lists.
'''

# Printing it as an object

values = [12, 18, 40, 60, 80, 120]

def remove40(x):
    return x > 40

print(filter(remove40, values))    


# Printing it as a list

values = [12, 18, 40, 60, 80, 120]

def remove40(x):
    return x > 40

print(list(filter(remove40, values)))   


# Using Lambda to reduce it to a single line code

values = [12, 18, 40, 60, 80, 120]

print(list(filter(lambda x: x > 40, values)))  