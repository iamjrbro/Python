'''
LISTS AND TUPLES

    Lists: are mutable, you can change things by the end of it, using, by example, the Append function. It's defined by [ ].
    Tuples: are immutable, you cannot change it. It's defined by ( ).
'''

# Identifying which one is which one

colors_list = ['black', 'blue', 'green', 'pink']
values_tuples = (20, 42, 80, 102)

print(type(colors_list))
print(type(values_tuples))


# Multipling the Tuples 

values_tuples = (20, 42, 80, 102)

twolists = values_tuples * 2
print(twolists)


# Trying to change a item of the Tuples list with Append

values_tuples = (20, 42, 80, 102)

values_tuples.append(90)

print(values_tuples)