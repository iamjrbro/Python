'''
LISTS - MANIPULATION

    1. to look for an specific information inside a list, you can use it's index (#1).
    2. keep in mind that positive numbers are from right to left, while negative numbers are from left to right (#2).
    3. if you want to change a specific info inside a list without making any alteration on it, you can look it throught index and change it (#3).
'''

# 1 
cities = ['Rio de Janeiro' , 'Fortaleza' , 'Palmas' , 'Recife']
# index        0                 1           2           3
print(cities[2])


#2
cities = ['Rio de Janeiro' , 'Fortaleza' , 'Palmas' , 'Recife']
# index        0                 1           2           3
print(cities[-0])


#3
cities = ['Rio de Janeiro', 'Fortaleza', 'Palmas', 'Recife']
# index        0                 1           2           3

cities[3] = 'Alagoas'
print(cities)