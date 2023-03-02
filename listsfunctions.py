'''
LISTS - FUNCTIONS

There functions that you can execute inside a list. You can find these fuctions on Pythons website.
'''

# Append: it append or add item x to the end of a list

cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife'] 

cities.append('São Paulo')

print(cities)


# Remove: it removes the user-specified item. It is very useful if we know the item

cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife'] 

cities.remove('Fortaleza')

print(cities)


# Insert: inserts the specified item x at index position i

cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife'] 

cities.insert(3,'Limeira')

print(cities)


# Pop: remove an item at a specified index and display the removed item. After removing, the remaining items moved forward to fill the index gap

cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife'] 

cities.pop(0)

print(cities)


# Sort: sort the items in Ascending order

cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife'] 

cities.sort()
print(cities)