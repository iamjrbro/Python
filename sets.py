'''
SETS

Sets are similiar to lists. However, they avoid duplicated itens and don't use index.
  1. it's defined by { }
  These are some examples of what you can do with Sets while using Operators.
'''

# Union | (it joins both lists without the repeated numbers)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)


# Difference - (it shows numbers that are present on the 1st list but not in the 2nd)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 - num2)


# Symmetric different ^ (remove all the duplicates numbers from both lists)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 ^ num2)


# And & (it shows the duplicated numbers from both lists)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(num1 & num2)


# Verifying the size of a list (how many itens there's on the list)

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 80]

num1 = set(list1)
num2 = set(list2)

print(len(num1))
print(len(num2))