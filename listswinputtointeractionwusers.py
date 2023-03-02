'''
LISTS - INPUT TO INTERACT WITH USERS

Using Input to check itens on a list.
'''

# Example where the user is able to check if there´s a color avaible on stock

color = input('Enter the desired color:')
colors = ['green', 'yellow', 'brown', 'red']

if color.lower() in colors:
    print('Available on stock')

else:
    print('No available at the moment')    