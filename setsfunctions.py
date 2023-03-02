'''
SETS - FUNCTIONS

These are some of the functions that you can do on Sets with the Operators.
   obs:
   Remove: if you try to remove something that's not in the Set, it will present you an error (#4).
   Discard: if you try to remove something that's not in the Set, it will print the list without any error (#6).
'''

# 1. Adding itens to a Set

s = {1, 2, 3, 4}
s.add(5)

print(s)


# 2. Updating a Set with some itens

s = {1, 2, 3, 4}
s.update({5, 6, 7, 8})

print(s)


# 3. Removing an item from a Set with Remove

s = {1, 2, 3, 4}
s.remove(2)

print(s)


# 4. Trying to remove an item that is not in the Set with Remove

s = {1, 2, 3, 4}
s.remove(8)

print(s)


# 5. Removing an item from a Set with Discard

s = {1, 2, 3, 4}
s.discard(1)

print(s)


# 6. Trying to remove an item that is not in the Set with Discard

s = {1, 2, 3, 4}
s.discard(8)

print(s)