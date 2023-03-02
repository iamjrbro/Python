'''
MAP FUNCTION WITH LAMBDA

Map + Lambda shorten the ammount of code line.
'''

# Map with Lambda

list1 = [1, 2, 3, 4]

list2 = map(lambda x: x * 2, list1)

print(list(list2))


# Reducing  it to a single line code

list1 = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, list1)))