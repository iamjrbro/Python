'''
DICTIONAY MANIPULATION

Manipulating data inside the Dictionary.
'''

# Updating infos

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

student.update({'name': 'Frederic', 'age': 16, 'approvement status': False})

print(student)


# Adding info

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

student.update({'adress' : '11321 Clover Avenue'})

print(student)


# Getting a info

student = {'name': 'Jaline', 'age': 18, 'final_grade': 'A', 'approvement status': True} 

student.get('approvement status')

print(student.get('approvement status'))


# Adding a list inside the dictionary

student = {
    'name': 'Jaline', 
'age': 18, 
'final_grade': 'A', 
'approvement status': True, 
'Classes': ['English', 'Chemistry', 'Mathematics', 'Biology']
} 

for keys, values in student.items():
    print(keys, values)