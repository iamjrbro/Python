'''
SLICE

  Extracts specific information from your code by making use of the index.
    1. the code will always come back according to the index you searched inside the brackets.
    2. the index will always start at number 0, so if you search, for example, the numbers 1 through 5, the result you will receive will be from 0 to 4 (example #3).
    3. if you want to search for information from one number to another, use : (example #3).
    4. if you want to search for specific information, use, (example #4).
    5. if you insert negative numbers into the brackets, you will receive the result from right to left (example #5).
'''


#1

fruit = 'Banana'
#index   012345

print(fruit[4])


#2

value = '102.90'
value = str(value)
#index   012345

print(value[4])


#3

value = '5'
value = (value)
#index   012345