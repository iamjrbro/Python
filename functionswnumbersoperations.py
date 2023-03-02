'''
FUNCTION - NUMBER OPERATIONS

    1. variables that are not within a function, are called global variables.
    2. in these examples, the variables are within the functions, referring to them.
    3. if you duplicate a function by using a similiar name and changing variables, Python recognizes that they are two different functions (#2).
'''

# Simple adding operation

def addnumbers():
    n1 = 2000
    n2 = 800
    result = n1 + n2
    print(result)

addnumbers()


 # 2. Simple adding operation, duplicating the function

def addnumbers():
    n1 = 2000
    n2 = 800
    result = n1 + n2
    print(result)   

def addnumbers2():
    n1 = 4000
    n2 = 444
    result = n1 + n2
    print(result)      

addnumbers2()    