'''
IF / ELIF / ELSE

    If: first conditional
    Elif: optional use
    Else: last conditional
'''

speed = 100

if speed > 120:
    print('Overspeed')
    print('Please, slow down')

elif speed < 60:
    print('Please, speed up')

else:
    print('You´re driving at a good speed. Have a safe ride! ')