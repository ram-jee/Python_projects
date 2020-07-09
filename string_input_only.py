# This code forces user to enter string inputs
# Integer inputs are discarded and user is asked to enter again


while True:
  try:
    x = input('Enter string: ')

    if int(x):
      x = input('Enter string: ')
      if int(x):
        continue
  except:
    break

print(x)
