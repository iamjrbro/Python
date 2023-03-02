'''
FUNCTION - DEFAULT AND NON-DEFAULT

    1. Default: you need to define the value in the parameter
    2. Non-default: you dont need to define the value in the parameter
        obs: In the parameter, non-default always comes before the default one.
'''

# This example uses Function, Parameters and Arguments

def welcome(name,quantity):
    print(f'Hello {name}.')
    print(f'We have {str (quantity)} laptops available')  


welcome('Hugo', 8)   


# This example uses 'name' as the non-default option

def welcome(quantity, name= 'Orochi'):
    print(f'Hello {name}.')
    print(f'We have {str (quantity)} laptops available')  

welcome(2)


# This example uses 'quantity' as the non-default option

def welcome(name, quantity = '6'):
    print(f'Hello {name}.')
    print(f'We have {str (quantity)} laptops available')  

welcome('Allison')