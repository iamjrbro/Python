'''
DICTIONARY WITH FOR LOOP

For Loop inside the dictionary.
'''

# Printing only the keys

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

for x in student.keys():
    print(x)


# Printing only the values

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

for x in student.values():
    print(x)


# Printing both, keys and values

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

for x in student.items():
    print(x)


# Printing both, keys and values, in a different way (it prints all in a single line)

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 
print(student)