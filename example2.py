'''
COOKING CALCULATOR

This code develops a program, using If/Else, that, based on the temperature of the steak (in Fahrenheit), returns the cooking point.
There's two examples below, one using on If/Elif/Else, and the other using If/Elif/Else + Range.
     -> the user must enter the temperature of the steak.

                Temperatures

                120°F  Rare
                130°F  Medium rare
                140°F  Medium
                150°F  Medium well
                160°F  Well done

obs: this example can also be found on the Calculators repository                 
'''

# Using only If/Elif/Else condition

temp = int(input('What is the temperature of the steak:'))

if temp <= 120:
    print('Your steak need to cook your steak for a few more minutes')

elif temp >= 120:
    print('Rare')

elif temp <= 130:
    print('Medium rare')   

elif temp <= 140:
    print('Medium')  

elif temp <= 150:
    print('Medium well')   

else:
    temp <= 160
    print('Well done')     



# Using If/Elif/Else condition + Range

temp2 = int(input('What is the temperature of the steak:'))


if temp2 < 120:
    print('Your steak need to cook for a few more minutes')
elif temp2 in range(120, 129):
    print('Rare')
elif temp2 in range(130, 139): 
    print('Medium rare') 
elif temp2 in range(140, 159):
    print('Medium well')
elif temp2 >= 160:
    print('Well done')