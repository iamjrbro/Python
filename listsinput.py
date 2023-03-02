'''
LISTS - INPUT

Lists using input to interact with users.
  1. the Split function used after 'fruits_user' makes the list possible, because it slipts the itens everytime that identifies a comma.
  -> the user has to type the list, seprating the itens by ','.
'''

# Example creating a list of fruits from the user's input

fruits_user = input('Please, type your list using commas to separate the itens:')

fruitlist = fruits_user.split(', ')

print(fruitlist)