'''
FUNCTIONS - X ARGS WITH PARAMETERS

Used when you are not sure how many parameters will be used in the program.
  1. in this one, you are able to define the parameters as you want, not having to altered the parameters at the begging of the code.
  2. allows you to choose the amount of parameters, how you are going to name them and which ones you want to use.
  3. to define it just add a ** in the parameter, before the argument.
'''

# These are examples where a dealership wants to store specific data from some cars

# one car only

def dealer(**car):
    return car

print (dealer(model = 'X1', color = 'black')) 


# multiple cars

def dealer2(**cars):
    return cars

print (dealer2(model = 'Porshe 911 Carrera', color = 'white'))  
print (dealer2(model = 'Mercdes AMG GT', board = 'F985L2')) 
print (dealer2(model = 'X1', color = 'black', price = '$53826,45', board = 'L1TT3H4IR')) 
print (dealer2(model = 'Lamborghini Veneno', price = '$4,5 m')) 