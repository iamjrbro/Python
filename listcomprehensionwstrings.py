'''
LIST COMPREHENSION WITH STRINGS

Used when you need to create a new list from an existing list.
'''

list1 = ['strawberry', 'banana', 'orange', 'coco']
list2 =[]

for x in list1:
    if 'a' in x:
        list2.append(x)

print(list2)        


# Reducing it to a single line code

list1 = ['strawberry', 'banana', 'orange', 'coco']
list2 =[]

list2 = [x for x in list1 if 'o' in x]

print(list2)  