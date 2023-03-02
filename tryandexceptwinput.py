'''
TRY AND EXCEPT WITH INPUT

    1. used in conducting tests in searches.
    2. does not stop the program.
    3. displays custom messages when it encounter an error.
'''

# Hypothetical situation where, if the user type a letter instead of a number on the 'Type the price of your product:' input, it will inform the user to type a value in numbers.

try:
    value = int(input('Type the price of your product:'))
    print(value)
except ValueError:
    print('Please, type a number')    