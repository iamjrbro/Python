'''
LISTS AND ARRAYS

Arrays shorten lists.

    obs: you have to import it.
    obs2: you can find Efficient arrays of numeric values on docs.python.org
    obs3: efficients used in this example:
      u: wchar_t
      i: signed int
      f: float
'''

# How is usually done

letters = ['a', 'b', 'c', 'd']
numbers_i = [10, 20, 30, 40]
numbers_f = [1.1, 1.2, 1.3, 1.5]

print(letters)
print(numbers_i)
print(numbers_f)
print()


# Arrays

from array import array

letters = array('u'['a', 'b', 'c', 'd'])
numbers_i = array('i'[10, 20, 30, 40])
numbers_f = array('f'[1.1, 1.2, 1.3, 1.5])

print(letters)
print(numbers_i)
print(numbers_f)