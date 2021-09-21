import time

def gen_func(num):

  for value in range(1,num):
#Yields 1 value at a time and then waits
    yield value


g  = gen_func(100)

for i in range(10):
  time.sleep(1)
#Prints one value yielded by generator at a time
  print(next(g))


