'''
LIST - ASSOCIATION WITH ZIP

It associates itens from different lists, one by one, using the Zip function.
'''

# Example using two lists (associating colors and values)

colors = ['black', 'blue', 'green', 'pink']
values = [20, 42, 80, 102]

twolists = zip(colors, values)

print(list(twolists))


# Example using four lists (weekend eatables for four different people)

fruits = ['blueberry', 'banana', 'strawberry', 'apple']
candy = ['bubblegum', 'fini', 'juice', 'pie']
drinks = ['coke', 'pepsi', 'vodka', 'gin']
food = ['strognoff', 'pizza', 'pasta', 'lasagna']

weekend = zip(fruits, candy, drinks, food)

print(list(weekend))