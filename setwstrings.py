'''
SETS WITH STRINGS

Basically the same as on the "sets.py" archive, but writing the code as strings.

    These are some examples of what you can do with Sets while using Operators and writing the code as strings.
'''

# Union | (it joins both lists without the repeated letters)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'d', 'e', 'f', 'g'}
set3 = {'g', 'h', 'i', 'j'}

set4 = set1.union(set3)

print(set4)


# Difference - (it shows all the letters that are present on the 1st list but not in the 2nd)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'d', 'e', 'f', 'g'}
set3 = {'g', 'h', 'i', 'j'}

set4 = set2.difference(set3)

print(set4)


# Symmetric different ^ (remove all the duplicates letters from both lists)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'d', 'e', 'f', 'g'}
set3 = {'g', 'h', 'i', 'j'}

set4 = set3.symmetric_difference(set2)

print(set4)


# And & (it shows the duplicated letters from both lists)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'d', 'e', 'f', 'g'}
set3 = {'g', 'h', 'i', 'j'}

set4 = set1.union(set3)

print(set4)