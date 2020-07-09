
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
