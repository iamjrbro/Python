'''
FUNCTIONS

  Blocks of code that will perform some kind of task or manipulation of data, and may or may not receive input data (parameters/arguments).
  Parameters are the names given to the attributes that a function can receive.
  Usually used to make it all easier, so you dont need to ctrl+c ctrl+v your codes when working with big projects.
    1. determined by the DEF condition
    2. when you create it, you have to give it a name. So when you want to call it, just type the name + ().
'''

# This is a message boot example using Functions

def welcome():
    print('Are you still interested on selling your product on our website?')

welcome()    


# This is an example were the Function is called inside the other code (here, Ive used the While Loop Condition + Function)

value = int(input('Please, type your product value:'))

while value > 600:
    value = (value * 0.10 + value)
    print(f'Your products final price will be ${value}')
    break

welcome()