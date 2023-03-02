'''
TRY AND EXCEPT

    1. used in conducting tests in searches.
    2. does not stop the program.
    3. displays custom messages when it encounter an error.
'''

# In this example,  a List, that works with Index, and I've try to look for a not existing Index

try:
    letters = ['a', 'b', 'c', 'd']
    print(letters[4])
except IndexError:
    print('This Index does not exist ')