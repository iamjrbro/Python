'''
WHILE LOOP

Usually used for loops that depend on a condition.
'''

# This example creates a sale promotion for a product, which will start with the sale price at $100 and will get $5 off every day. However, the loop ends when the value reaches the $20 limit.

value = 100
day = 0

while value > 20:
    day += 1
    print(f'At day {day} the product will be sold for ${value}')
    value -= 5