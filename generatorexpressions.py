'''
GENERATOR EXPRESSIONS

    1. easier and faster way to write Lists, Dictionaries, etc.
    2. it consumes less memory (in bytes).
'''

# How it's usually done

numbers = [x * 10 for x in range(10)]
print(numbers)


# Checking if it's classification (in this case, it's a List)

numbers = [x * 10 for x in range(10)]
print(type(numbers))
print(numbers)


# Generator Expressions (printing it as an object)

numbers = (x * 10 for x in range(10))
print(numbers)


# Generator Expressions (printing it as a list)

numbers = (x * 10 for x in range(10))
print(list(numbers))


# Checking if it's classification (in this case, it's a Generator Expressions)

numbers = (x * 10 for x in range(10))
print(type(numbers))