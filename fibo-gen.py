def fibo(number):
  a = 0
  b = 1

  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp+b
    

g = fibo(20)

for i in range(20):
  print(next(g))
