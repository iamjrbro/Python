'''
FOR LOOP - NESTED LOOPS

A loop inside another.
'''

# outer loop
# inner loop

'''
In this case, the first loop will execute the first number/letter/sentence and the loop within it will run completely, then the first loop will execute the second number/letter/sentence, and the second will run completely again, and so on
'''

# 1

for number1 in range(5):
    print(number1)
    for number2 in range(5):
        print(number2)



# 2

for number1 in range(5):
    print(number1)
    for number2 in range(5):
        print(number1,number2)
        for number3 in range(5):
            print(number1,number2,number3)
            for number4 in range(5):
                print(number1,number2,number3,number4)



 # 3

for number1 in range(3):
    print(number1)
    for number2 in range(5):
        print(number1,number2)
        for number3 in range(7):
            print(number1,number2,number3)
            for number4 in range(9):
                print(number1,number2,number3,number4)      