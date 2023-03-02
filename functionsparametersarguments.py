'''
FUNCTIONS - PARAMETERS ARGUMENTS 

Used to create a repetitions, using less code line.
    -> in this situation, a message boot for 4 different clients will be used as example
'''

# This example uses Function (without Parameters and Arguments)

def welcome1():
    print('Hello Noah')
    print('We have 6 laptops available')


def welcome2():
    print('Hello Julia')
    print('We have 5 laptops available')    


def welcome3():
    print('Hello Kylie')
    print('We have 4 laptops available')    


def welcome4():
    print('Hello Stephan')
    print('We have 3 laptops available')   

welcome1()    
welcome2()
welcome3()
welcome4()


# This example uses Function, Parameters and Arguments

def welcome(name,quantity):
    print(f'Hello {name}.')
    print(f'We have {str (quantity)} laptops available')  

welcome('Noah', 6) 
welcome('Julia', 5) 
welcome('Kylie', 4) 
welcome('Stephan', 3) 