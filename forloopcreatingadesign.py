'''
FOR LOOP - CREATING A DESIGN

Used to creat a design with the Range function.
'''

'''
@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@
'''

# This example creates a 30x6 rectangle and the symbol used was @

lines = 6
columns = 20
symbol = '@'

for l in range(lines):
    for c in range(columns):
        print(symbol, end = ' ')
    print()