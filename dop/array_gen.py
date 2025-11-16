import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: int = None) -> list[int]:
    """
    Генерирует массив случайных целых чисел
    """
    if n < 0:
        raise ValueError("Отрицательное n")
    if lo > hi:
        raise ValueError("Выход за границы")
    if distinct and (hi - lo + 1) < n:
        raise ValueError("Ошибка уникальных значений")
    
    if seed is not None:
        random.seed(seed)
    
    if distinct:
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for i in range(n)]




def nearly_sorted(n: int, swaps: int, *, seed: int = None) -> list[int]:
    """
    Создает почти отсортированный массив
    """
    if n < 0:
        raise ValueError("Отрицательное n")
    if swaps < 0:
        raise ValueError("Отрицательное swzps")
    
    if seed is not None:
        random.seed(seed)

    a = list(range(n))

    for g in range(swaps):
        i, j = random.sample(range(n), 2)
        a[i], a[j] = a[j], a[i]
    
    return a




def many_duplicates(n: int, k_unique: int = 5, *, seed: int = None) -> list[int]:
    """
    Создает массив с редкими уникальными
    """
    if n < 0:
        raise ValueError("Отрицательное n")
    if k_unique <= 0:
        raise ValueError("Отрицательное k_unique")
    
    if seed is not None:
        random.seed(seed)

    u_val = random.sample(range(1, 10000), k_unique)
    return [random.choice(u_val) for i in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Создает полностью обратно отсортированный массив
    """
    if n < 0:
        raise ValueError("Отрицательное n")
    
    return list(range(n-1, -1, -1))




def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed: int = None) -> list[float]:
    """
    Генерирует массив случайных вещественных чисел
    """
    if n < 0:
        raise ValueError("Отрицательное n")
    if lo > hi:
        raise ValueError("Выход за границы")
    
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for i in range(n)]

