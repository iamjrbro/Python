'''
WHILE LOOP CONDITION

Hypothetical ecommerce which has a 10% commission on top of the price of the product, if it has a value above $20.
In this example, the loop has a break, that will stop the loop as soon as the result of the calculation return to the user.
'''

value = int(input('Please, type your product value:'))

while value > 20:
    value = (value * 0.10 + value)
    print(f'Your products final price will be ${value}')
    break