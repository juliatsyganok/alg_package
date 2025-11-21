def bubble_sort(a: list[int]) -> list[int]:
    """
    Пузырьковая сортировка
    Лучший: O(n), Средний: O(n²), Худший: O(n²)
    """
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a



def quick_sort(a: list[int]) -> list[int]:
    """
    Быстрая сортировка
    Лучший: O(n log n), Средний: O(n log n), Худший: O(n²)
    """
    if len(a) <= 1:
        return a
    else:
        q = a[0]
        left = []
        ravn = []
        right = []
        for el in a:
            if el < q:
                left.append(el) 
            elif el > q: 
                right.append(el) 
            else: 
                ravn.append(el)
        return quick_sort(left) + ravn + quick_sort(right)
    


def counting_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчётом
    Всегда O(n + k), где k - диапазон
    """
    mi = min(a)
    ma = max(a)
    
    len_m = ma - mi + 1
    count = [0] * len_m
    
    for i in a:
        count[i - mi] += 1
    
    k = 0
    for i in range(len_m):
        for j in range(count[i]):
            a[k] = i + mi
            k += 1
    
    return a



def radix_sort(a: list[int], base: int=10) -> list[int]:
    """
    Поразрядная сортировка
    Всегда O(n * k)
    """
    m_v = max(a)
    dg = 1
    
    while m_v // dg > 0:
        m = [[] for i in range(base)]
        for i in a:
            idx = (i // dg) % base
            m[idx].append(i)
        a = []
        for bucket in m:
            a.extend(bucket)
        dg *= base
    
    return a



def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортировка по категориям
    Лучший: O(n + k), Средний: O(n + k), Худший: O(n²)
    """
    n = len(a)
    if n <= 1:
        return a
    buckets = [[] for _ in range(10)]
    for num in a:
        bucket_index = int(num * 10)
        if bucket_index == 10:
            bucket_index = 9
        buckets[bucket_index].append(num)
    result = []
    for bucket in buckets:
        if len(bucket) > 1:
            result.extend(bucket_sort(bucket))
        else:
            result.extend(bucket)
    return a




def heap_sort(a: list[int]) -> list[int]:
    """
    Пирамидальная сортировка
    Всегда O(n log n)
    """
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heap(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap(a, i, 0)
    
    return a

def heap(a, n, i):
    """
    Для построения дерева
    """
    lg = i 
    left = 2 * i + 1 
    right = 2 * i + 2 
    if left < n and a[left] > a[lg]:
        lg = left
    if right < n and a[right] > a[lg]:
        lg = right
    if lg != i:
        a[i], a[lg] = a[lg], a[i]
        heap(a, n, lg)   
