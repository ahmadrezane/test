def fib(n):
    a = 0
    b = 1
    for i  in range(n):
       b, a = a + b, b
    return a 

def se (a, b):
    s = a + b * 8
    print(s)

    