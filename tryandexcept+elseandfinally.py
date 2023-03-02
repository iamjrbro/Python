'''
TRY AND EXCEPT + ELSE AND FINALLY

Hypothetical situation where, if the user type a letter instead of a number on the 'Type the price of your product:' input, it will inform the user to type a value in numbers.
'''

# ELSE: in this example, the Finally condition will only be executed if the Try condition is right

try:
    value = int(input('Type the price of your product:'))
    print(value)
except ValueError:
    print('Please, type a number') 
else:
    result = value * 20
    print(result)    


# FINALLY: in this example, the Else condition will only be executed if the Try condition is right

try:
    value = int(input('Type the price of your product:'))
    print(value)
except ValueError:
    print('Please, type a number')    
finally:
    print('Thank you')
except ValueError:
    print('Please, type a number')    
finally:
    print('Thank you')     