def fib(n):
    a = 0
    b = 1
    for i  in range(n):
       b, a = a + b, b
    return a 

print(fib(9))