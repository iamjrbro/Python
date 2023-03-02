'''
FOR LOOP - STRINGS
'''

# to print letter by letter

for letter in 'Inevitable':
    print(letter)


# to print letter by letter, but associating the word to a variable instead of writing it twice

word = 'Inevitable'
for letter in word:
    print(letter)  


# to print letter by letter + some text

word = 'Inevitable'
for letter in word:
 print(f'{letter}' ' ' 'is inside the word Inevitable')


# to print letter by letter, associating the word to a variable instead of writing it twice, but I used it with one of my favorites songs, Favorita by Yunk Vino

 song = 'Eu me perco na sua vista Relaxa, meu bem, cê sabe que você é a minha favorita Desce gin, whisky Bourbon, tá bom Eu não me sinto tão normal você pode ver Preciso desse ritual pra sobreviver Eu me perco na sua vista Relaxa, meu bem, cê sabe que você é a minha favorita Desce pill, whisky Bourbon, tá bom Eu não me sinto tão normal você pode ver Preciso desse ritual pra sobreviver'
for text in song:
 print(text)