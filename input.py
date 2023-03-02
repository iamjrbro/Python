'''
INPUT

Allows people to interact with the program by entering information using the input condition.
  obs: age is a int (number) and was converted to a str (text)
'''

name = input('Whats your name?: ')
age = input('How old are you?: ')
city = input('Where do you live?: ')

print (name + ' is ' + str(age) + ' years old and lives at ' + city)