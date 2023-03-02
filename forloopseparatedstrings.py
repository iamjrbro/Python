'''
FOR LOOP - SEPARATED STRINGS

Used to insert a space between each letter of the word (#2).
'''

# 1. modifing the word LIFE to L I F E (in this example, the letters will be one below the other)

word = 'LIFE'

for space in word:
    print(space)


# 2. modifying the word LIFE to L I F E (this example is applying For Loop to Separated Strings, which applies the spaces between the letters and leaves it in a single line
word = 'LIFE'

for space in word:
    print(f'{space}' , end= ' ')