def factorial(n: int) -> int:
    """
    Получение факториала числа циклом
    """
    if n < 0:
        raise ValueError("Неверное число")
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i
    return cnt



def factorial_recursive(n: int) -> int:
    """
    Получение факторила числа рекурсивно
    """
    if n < 0:
        raise ValueError("Неверное число")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)



def fibo(n: int) -> int:
    """
    Получение числа Фибоначи по номеру циклом
    """
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
    """
    Получение числа Фибоначчи по номеру рекурсивно
    """
    if n < 0:
        raise ValueError("Неверное число")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

