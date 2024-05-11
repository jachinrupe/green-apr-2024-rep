secret_number = 1994
print('''
=========================
===SECRET NUMBER GAME ===
=========================
''')
user_input = int(input('Try to guess the year when Python 1.0 was released: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the year when Python 1.0 was released:'))
print('Perfect! You have guessed the secret number.')