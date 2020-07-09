import random

print('Levels: 2-Easy, 5-Medium, 10-Challenge')
level = int(input('Enter level: '))
computer_val = random.randint(1,level)
attempts = 1
user_val = int(input('Enter choice: '))

while True:
  if computer_val == user_val:
    print('\nYou Won! Congratulations')
    print(f'Expected: {computer_val} entererd: {user_val}')
    print(f'Attempts: {attempts}')
    break
  else:
    attempts += 1
    print(f'\nYou Lost! \nExpected: {computer_val} entererd: {user_val}')
    repeat = input('Want to try again, Yes or No?').lower()
    if repeat == 'no':
      print('Thank you for playing!')
      break
    else:
      computer_val = random.randint(1,level)
      user_val = int(input('Enter choice: '))

