'''
LOGICAL OPERATORS

Used to print a message according to true/false and the conditions that you putted inside your variable.
    1. you can use 'and' or 'or' in this on the If condition
'''
# Hypothetical bank financial


# True with and

income_above_10k = True
clean_name = True

if income_above_10k and clean_name:
 print('Funding approved')

else:
 print('Funding denied')


# True with or

income_above_10k = True
clean_name = True

if income_above_10k or clean_name:
 print('Funding approved')

else:
 print('Funding denied')


# True/False

income_above_10k = True
clean_name = False

if income_above_10k and clean_name:
 print('Funding approved')

else:
 print('Funding denied')


# False/True

income_above_10k = False
clean_name = True

if income_above_10k and clean_name:
 print('Funding approved')

else:
 print('Funding denied')


# False/False with and

income_above_10k = False
clean_name = False

if income_above_10k and clean_name:
 print('Funding approved')

else:
 print('Funding denied')


# False/False with or

income_above_10k = False
clean_name = False

if income_above_10k or clean_name:
 print('Funding approved')

else:
 print('Funding denied')