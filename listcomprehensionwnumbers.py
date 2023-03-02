'''
LIST COMPREHENSION WITH NUMBERS

In this example, a list is putted inside a range, which is determined to run 6 times. Everytime the range runs, it will multiply by 10.
'''

# How is usually done 

values = []

for x in range(6):
    values.append(x*10)

print(values)    


# Using List Comprehension to it reduce to a single line code

values = [x*10 for x in range(6)]
print(values)    