def countingSort(arr):
    mi = min(arr)
    ma = max(arr)
    
    len_m = ma - mi + 1
    count = [0] * len_m
    
    for i in arr:
        count[i - mi] += 1
    
    k = 0
    for i in range(len_m):
        for j in range(count[i]):
            arr[k] = i + mi
            k += 1
    
    return arr