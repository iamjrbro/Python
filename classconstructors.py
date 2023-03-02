'''
CLASS CONSTRUCTORS

Used to shorten code.
1. Class Constructors are used to shorten code by creating the Parameter inside the object.
2. it's executation is possible due to the Self function, that will associate the Parameters with each Object, not matter how many Objects you define.
'''

# creating the Class 

class Employee:
   def __init__(self, name, last_name, birthday, email, cellphone, adress):
    self.name = name
    self.last_name = last_name
    self.birthday = birthday
    self.email = email
    self.cellphone = cellphone
    self.adress = adress


# creating the Object 

employee1 = Employee('Jesse', 'Rose', '01/08/1994', 'jsk8@gmail.com', '808563368', '918 Saint George st')
employee2 = Employee('Cristal', 'MCallin', '12/04/1996', 'cristal22@gmail.com', '228866330', '818 George Blvr')
employee3 = Employee('Abel', 'Machado', '17/08/2000', 'am@gmail.com', '895214565', '303 Roger Crallin st')
employee4 = Employee('Sabrina', 'Delfante', '03/06/2002', 'delfantes@gmail.com', '236552014', '32 Leviano Blvr')


# printing employee1

print(employee1.name)
print(employee1.last_name)
print(employee1.birthday)
print(employee1.email)
print(employee1.cellphone)
print(employee1.adress)


# printing employee2

print(employee2.name)
print(employee2.last_name)
print(employee2.birthday)
print(employee2.email)
print(employee2.cellphone)
print(employee2.adress)


# printing employee3

print(employee3.name)
print(employee3.last_name)
print(employee3.birthday)
print(employee3.email)
print(employee3.cellphone)
print(employee3.adress)


# printing employee4

print(employee4.name)
print(employee4.last_name)
print(employee4.birthday)
print(employee4.email)
print(employee4.cellphone)
print(employee4.adress)