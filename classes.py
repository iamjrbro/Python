'''
CLASSES

    1. Classes are used to group data and functions and can be reused;
    2. objects are parts inside a Class (instances);
    3. used to creat objects (instances);
    4. a Class name will always start with capital letter.
'''

# In this example, you cannot add another employee because the parameters are directly within the Class
# Class = employee and Objects = name, last name, birthday, email, cellphone number and adress

class Employee:
    name ='Jesse'
    last_name = 'Rose'
    birthday = '01/08/1994'
    email = 'jsk8@gmail.com'
    cellphone = '808563368'
    adress = '918 Saint George st'

employee1 = Employee()    

print(employee1.name)
print(employee1.last_name)
print(employee1.birthday)
print(employee1.email)
print(employee1.cellphone)
print(employee1.adress)