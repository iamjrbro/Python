'''
LISTS CONCATENATION

Adding a list inside another.
'''

# 1. Multipling a list by 4

numbers = [1, 2, 3, 4]

final = numbers * 4
print(final)


# 2. Adding two different lists

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

final = numbers + letters
print(final)


# 3. Adding two different lists (same as #2), but using the extend function

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

numbers.extend(letters)
print(numbers)


# 4. Adding two different lists and multipling one of them

numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

final = numbers + letters * 6
print(final)


# 5. Adding a list inside a list

names = [['Julia', 'Leo'], ['Keyla', 'Adriana']]

print(names)


# 6. Adding a list inside a list, put looking for specific infos using index and itens (in this example, index 0)

# index          0                 1
names = [['Julia', 'Leo'], ['Keyla', 'Adriana']]
# itens      0       1         0         1

print(names[0])


# 7. Adding a list inside a list, put looking for specific infos using index and itens (in this example, index 1 and item 1)


# index          0                 1
names = [['Julia', 'Leo'], ['Keyla', 'Adriana']]
# itens      0       1         0         1

print(names[1][1])


# 8. Adding a list inside a list, put looking for specific infos using index and itens (in this example, I used numbers as itens)


# index   0          1
age = [[18, 22], [19, 24]]
# itens 0   1      0   1

print(age[1])


# index   0          1
age = [[18, 22], [19, 24]]
# itens 0   1      0   1

print(age[0][1])