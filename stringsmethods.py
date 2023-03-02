'''
STRING METHODS

Used to make changes to its variable, having several options for modifications, such as these in the examples below.
'''

# find a letter

message = 'I love listening to music'

print(message.find('m'))


# find the position of a letter

message = 'I love listening to music'
#index 0123456789 

print(message.find('e'))


# replace one letter with another in a word

message = 'I love listening to music'

print(message.replace('e', 'j'))


# replace one word with another

message = 'I love listening to music'

print(message.replace('music', 'trap'))


# put every message in caps

message = 'I love listening to music'

print(message.capitalize())