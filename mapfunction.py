'''
MAP FUNCTION

    1. used to apply a function to an iterable, per item (list, tuple, dictionary, etc.).
    2. it's generally, used with Lists.
'''

# Printing it as an object

list1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

list2 = map(multi, list1)

print(list2)


# Printing it as a list

list1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

list2 = map(multi, list1)

print(list(list2))