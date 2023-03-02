'''
FORMATED STRINGS

Used to shorten code.
'''

# how is usually done

name = 'Pablo'
lastname = 'Borges'
profession = 'Developer'

text = ' ' + name + ' ' + lastname + 'is an excelent ' + ' [+ profession]'

print(text)


# using Formated Strings

name = 'Pablo'
lastname = 'Borges'
profession = 'Developer'

text2 = f'O {name} {lastname} is an excelent [{profession}]'

print(text2)