def countingSort(arr):
    m = [0] * 100
    for i in arr:
        m[i] += 1
    return m