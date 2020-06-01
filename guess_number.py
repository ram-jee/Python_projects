


from random import randint



while True:
  n = int(input('Enter pool size: '))
  answer = randint(1,n)

  guess = int(input('Enter your number: '))

  if 0 < guess < n:
    if guess == answer:
      print(" \n             YOU WON :)")
      break
    else:
      print(f'YOU LOST :( right number is {answer}')
      chance = input(print('\nDo you want one more chance? Y or N?'))
      if chance.lower() == 'y':
        continue
      else:
        break
