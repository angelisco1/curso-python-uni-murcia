def fibo(n):
  serie_fib = [0]
  a = 0
  b = 1
  i = 0

  while i < n - 1:
    serie_fib.append(b)
    a, b = b, a + b
    i += 1

  return serie_fib


if __name__ == '__main__':
  print(fibo(3))
  print(fibo(5))

  # fibo(5) -> [0, 1, 1, 2, 3]
  # [0, 1, 1, 2, 3, 5, 8, ...]
  # unpacking
