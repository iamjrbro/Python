'''
CLASS CONSTRUCTORS + MORE FUNTIONS

    1. in the following examples, a new Def will be created so Name and Last name can be in the same line (Full name).
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

    def fullname(self): 
        return self.name + ' ' + self.last_name


# creating the Object 

employee1 = Employee('Jesse', 'Rose', '01/08/1994', 'jsk8@gmail.com', '808563368', '918 Saint George st')
employee2 = Employee('Cristal', 'MCallin', '12/04/1996', 'cristal22@gmail.com', '228866330', '818 George Blvr')
employee3 = Employee('Abel', 'Machado', '17/08/2000', 'am@gmail.com', '895214565', '303 Roger Crallin st')
employee4 = Employee('Sabrina', 'Delfante', '03/06/2002', 'delfantes@gmail.com', '236552014', '32 Leviano Blvr')

print(Employee.fullname(employee1))