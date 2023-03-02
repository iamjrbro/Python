'''
FUNCTIONS - X ARGS

  X ARGS: multiple arguments

Commonly used when you are not sure of how many arguments will be used in the program.
  1. to define it just add a * in the parameter, before the argument.
  2. the data is set inside a variable.
  3. in this, a 'for loop' has to be used to execute the operations and a 'return' has to be used to get the results.
  4. in this example, 'return = 0' because its the start point of the 'for loop' , which is always gonna run every number setled inside the variable, one by one, and add it to result (#1). However, you can always change the number used in 'result' and it will be add in the end (#2).
'''

# 1
def add (*numbers):
  result = 0
  for num in numbers:
      result += num
  return result

x = add(2,3,4,7,4)  
print(x)


# 2

def add2 (*numbers):
  result = 6
  for num in numbers:
      result += num
  return result
  

y = add2(2,3,4,7,4)  
print(y)


# printing add1 and add2 

print(x,y)


# printing add1 + add2 

print(x+y)


# printing add1 - add2 

print(x-y)


# printing add1 * add2 

print(x*y)


# printing add1 / add2 

print(x/y)