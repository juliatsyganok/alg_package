def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a



def quick_sort(a: list[int]) -> list[int]:
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
    m = [0] * (len(set(a)) + 1)
    for i in range(len(a)):
        m[a[i]] += 1
        a[i] = 0
    k = 0
    for i in range(len(m)):
        while m[i] != 0:
            a[k] = i
            k += 1
            m[i] -= 1
    return a



<<<<<<< HEAD
def radix_sort(a: list[int], base: int = 10) -> list[int]:
=======
def radix_sort(a: list[int], base: int=10) -> list[int]:
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
>>>>>>> a994b5139de651ab6fa5e5141fef5a8ba14f325a
    return a




<<<<<<< HEAD
=======


def heap_sort(a: list[int]) -> list[int]:
>>>>>>> a994b5139de651ab6fa5e5141fef5a8ba14f325a
    
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heap(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap(a, i, 0)
    
    return a

def heap(a, n, i):
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
