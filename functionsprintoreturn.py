'''
FUNCTIONS - PRINT AND RETURN

    Print: performs a job. It does not store the information, either its variable. This function returns a value on the screen, but not on the program itself. Great for performing tasks because it uses code to run on screen and doesnt save it.
    Return: calculates and returns a value, storing its variable, but does not print on the screen without being prompted. Its the best option if you want to use the same data later, because 'return' saves your variable in the memory.
'''

# Print

def client1 (name):
    print(f'Hello {name}')

client1('Vanessa')     


# Return

def client2 (name):
    return(f'Hello {name}')

client2('Bruce')    


# Both

def client1 (name):
    print(f'Hello {name}')

x = client1('Vanessa')     


def client2 (name):
    return(f'Hello {name}')

y = client2('Bruce')    

print(x)
print(y)