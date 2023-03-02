'''
MULTIPLE COMPARISON OPERATORS

Used to shorten if/else statements while using multiple comparision operators.
'''

# Hypothetical case where a site only accepts to sell products that costs more than $20 and less than $40


#1 product not accept

value = 8

if 20 <= value < 40:
    print('Product accept')

else:
    print('Product not accept')

    
#2 product accept
    
value = 22

if 20 <= value < 40:
    print('Product accept')

else:
    print('Product not accept')