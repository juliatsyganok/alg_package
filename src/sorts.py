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



        
    
