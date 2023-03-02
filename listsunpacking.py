'''
LISTS - UNPACKING

Used to extract informations from lists and shortten code.
'''

# How is usually done

products = ('Banana', 'Blueberry', 'Apple', 'Coco')

item1 = products[0]
item2 = products[1]
item3 = products[2]
item4 = products[3]

print(item1)
print(item2)
print(item3)
print(item4)


# How you can do

products = ('Banana', 'Blueberry', 'Apple', 'Coco')

item1 , item2 , item3, item4 = products

print(item1)
print(item2)
print(item3)
print(item4)


# You can also remove some itens

products = ('Banana', 'Blueberry', 'Apple', 'Coco')

item1 , item2 , item3, *others = products

print(item1)
print(item2)
print(item3)