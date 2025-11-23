 Отчёт по лабораторной работе №3

 Тема: Алгоритмический мини-пакет (структуры данных и сортировки)

 1. Факториал и Фибоначчи

Реализованы функции:
- `factorial(n: int) -> int` - вычисление факториала итеративным методом
- `factorial_recursive(n: int) -> int` - вычисление факториала рекурсивным методом
- `fib(n: int) -> int` - вычисление числа Фибоначчи итеративным методом
- `fib_recursive(n: int) -> int` - вычисление числа Фибоначчи рекурсивным методом

Описание:
- Все функции принимают целочисленный аргумент n и возвращают целочисленный результат
- Реализована обработка граничных случаев (n = 0, n = 1)
- Добавлена проверка на отрицательные значения с выбрасыванием исключения ValueError

 2. Алгоритмы сортировки

Реализованы функции сортировки:
- `bubble_sort(arr: list[int]) -> list[int]` - сортировка пузырьком
- `quick_sort(arr: list[int]) -> list[int]` - быстрая сортировка
- `counting_sort(arr: list[int]) -> list[int]` - сортировка подсчетом
- `radix_sort(arr: list[int], base: int = 10) -> list[int]` - поразрядная сортировка
- `bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]` - блочная сортировка
- `heap_sort(arr: list[int]) -> list[int]` - пирамидальная сортировка

Особенности реализации:
- Все функции возвращают новый отсортированный список
- Соблюдено ограничение: не используются встроенные list.sort() и sorted()

 3. Структуры данных

Класс Stack (реализация на списке):
- `__init__(self)` - инициализация стека
- `push(self, x: int) -> None` - добавление элемента в стек
- `pop(self) -> int` - извлечение элемента из стека (выбрасывает IndexError при пустом стеке)
- `is_empty(self) -> bool` - проверка на пустоту
- `__len__(self) -> int` - получение размера стека
- `min(self) -> int` - получение минимального элемента (реализовано за O(1))

Класс Queue (реализация на списке):
- `__init__(self)` - инициализация очереди
- `enqueue(self, x: int) -> None` - добавление элемента в очередь
- `dequeue(self) -> int` - извлечение элемента из очереди (выбрасывает IndexError при пустой очереди)
- `front(self) -> int` - просмотр первого элемента (выбрасывает IndexError при пустой очереди)
- `is_empty(self) -> bool` - проверка на пустоту
- `__len__(self) -> int` - получение размера очереди

 4. Генераторы массивов

Реализованы функции генерации тестовых данных:
- `rand_int_array(n: int, lo: int, hi: int, , distinct=False, seed=None) -> list[int]` - генерация случайного целочисленного массива
- `nearly_sorted(n: int, swaps: int, , seed=None) -> list[int]` - генерация почти отсортированного массива
- `many_duplicates(n: int, k_unique=5, , seed=None) -> list[int]` - генерация массива с множеством дубликатов
- `reverse_sorted(n: int) -> list[int]` - генерация обратно отсортированного массива
- `rand_float_array(n: int, lo=0.0, hi=10.0, , seed=None) -> list[float]` - генерация случайного массива float

 5. Бенчмаркинг

Реализованы функции для тестирования производительности:
- `timeit_once(func, args, kwargs) -> float` - измерение времени выполнения одной функции
- `benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]` - сравнительный анализ алгоритмов сортировки

LEETCODE: (скрины выполненных задач)
1) LeetCode 509 Fibonacci Number
<img width="2156" height="1337" alt="image" src="https://github.com/user-attachments/assets/313447b0-02d5-49bb-8bd9-79729e78503a" />

2) LeetCode 70 Climbing Stair
<img width="2427" height="1340" alt="image" src="https://github.com/user-attachments/assets/f235f3c5-3405-424c-833d-89d57cbfde34" />

3)LeetCode 75 Sort Colors
<img width="2567" height="1340" alt="image" src="https://github.com/user-attachments/assets/7e585700-3628-4e29-909b-a02feccd97e0" />

4)Hackerrank CountingSort 1
<img width="1622" height="904" alt="image" src="https://github.com/user-attachments/assets/34b54e27-f956-4426-989f-2fee36055018" />

5)Hackerrank CountingSort 2
<img width="1584" height="917" alt="image" src="https://github.com/user-attachments/assets/8850912f-994a-4011-9c22-12d8fcca46d2" />

6)Hackerrank CountingSort 3

7)Hackerrank QuickSort 1

8)Top K Frequent Elements

9)K-th Largest Element in Array

10)LeetCode 20 Valid Parentheses

11)LeetCode 225 Implement Stack using Queues

12)LeetCode 232 Implement Queue using Stacks


