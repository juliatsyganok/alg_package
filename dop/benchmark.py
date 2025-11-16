import time

def timer_once(func, *args, **kwargs):
    """
    Измеряет время выполнения функции один раз
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start




def benchmark_sorts(arrays, algos):
    """
    Сравнивает производительность алгоритмов сортировки на разных массивах
    """
    res = {}
    for alg, f in algos.items():
        res[alg] = {}
        for arr, data in arrays.items():
            test = data.copy()
            time = timer_once(f, test)
            res[alg][arr] = time
    return res

