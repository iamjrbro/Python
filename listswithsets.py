'''
SETS

This code develops a program that generate 3 lists according to the needs below:

    list1 = employees that own a car and work on the night shift
    list2 = employees that own a car and work on the day shift
    list3 = employees that don't own a car
'''

employee = {'Jaline', 'Pablo', 'Daniel', 'Carlos', 'Roberta', 'Borges', 'Hailey', 'Marcela'}
day_shift = {'Jaline', 'Daniel', 'Pablo', 'Hailey'}
night_shift = {'Carlos', 'Roberta', 'Borges', 'Marcela'}
own_a_car = {'Jaline', 'Roberta', 'Daniel', 'Pablo'}


# list1 = employees that own a car and work on the night shift

night_shift_own_car = night_shift.__and__(own_a_car)
print(night_shift_own_car)


# list2 = employees that own a car and work on the day shift

day_shift_own_car = day_shift.__and__(own_a_car)
print(day_shift_own_car)


# list3 = employees that don't own a car

not_car = employee.difference(own_a_car)
print(not_car)



'''
 YOU CAN ALSO DO LIKE THIS

 In the follow examples, instead of creating a new variable, "Set" is used
'''

employee2 = {'Jaline', 'Pablo', 'Daniel', 'Carlos', 'Roberta', 'Borges', 'Hailey', 'Marcela'}
day_shift2 = {'Jaline', 'Daniel', 'Pablo', 'Hailey'}
night_shift2 = {'Carlos', 'Roberta', 'Borges', 'Marcela'}
own_a_car2 = {'Jaline', 'Roberta', 'Daniel', 'Pablo'}


# list1 = employees that own a car and work on the night shift

list1 = set(own_a_car2).intersection(night_shift2)
print(list1)


# list2 = employees that own a car and work on the day shift

list2 = set(own_a_car2).intersection(day_shift2)
print(list2)

# list3 = employees that don't own a car

list3 = set(employee2).difference(own_a_car2)
print(list3)