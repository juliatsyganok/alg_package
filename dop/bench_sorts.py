import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from sorts import *
from benchmark import benchmark_sorts
from array_gen import *

a = {
    "s": rand_int_array(100, 0, 1000),
    "m": rand_int_array(1000, 0, 1000),
    "l": rand_int_array(5000, 0, 1000)
}


alg = {
    "bubble": bubble_sort,
    "quick": quick_sort,
    "count": counting_sort,
    "radix": radix_sort,
    "heap": heap_sort
}

res = benchmark_sorts(a, alg)

print("Время: ")
for i in res:
    print(f"{i}:")
    for t in res[i]:
        print(f"  {t}: {res[i][t]:.6f}")