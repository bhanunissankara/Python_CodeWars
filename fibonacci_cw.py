def fibonacci(n):
    fib = 0
    if n in [0, 1]:
        return n
    for i in range(n+1):
        fib = i + fib
    return fib

    # if n in [0, 1]:
    #     return n
    # return fibonacci(n - 1) + fibonacci(n - 2)

    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

print(fibonacci(100))