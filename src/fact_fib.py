def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Неверное число")
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i
    return cnt



def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Неверное число")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)



def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("Неверное число")
    if n == 0:
        return 0
    if n == 1:
        return 1
    x, y = 0, 1
    for i in range(2, n + 1):
        x, y = y, x + y
    return y



def fibo_recursive(n: int) -> int:
    if cash is None:
        cash = {}

    if n < 0:
        raise ValueError("Неверное число")
    if n in cash:
        return cash[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    cash[n] = fibo_recursive(n - 1, cash) + fibo_recursive(n - 2, cash)
    return cash[n]

