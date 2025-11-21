import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from sorts import *
from fact_fib import *
from stack import Stack
from queue import Queue

def main():
    while True:
        print("1 - Сортировки")
        print("2 - Факториал")
        print("3 - Фибоначчи") 
        print("4 - Стек")
        print("5 - Очередь")
        print("0 - Выход")
        
        ch = input("Ввод: ")
        
        if ch == "1":
            a = list(map(int, input().split()))
            print("1-пузырьковая, 2-быстрая, 3-подсчётом, 4-поразрядная, 5-по категорям, 6-пирамидальная")
            s_tp = input()
            
            sorts = {
                "1": bubble_sort,
                "2": quick_sort, 
                "3": counting_sort,
                "4": radix_sort,
                "5": bucket_sort,
                "6": heap_sort
            }
            
            if s_tp in sorts:
                result = sorts[s_tp](a.copy())
                print(result)
            else:
                print("Ошибка ввода")
                
        elif ch == "2":
            n = int(input())
            print(f"Рекурсия: {factorial_recursive(n)}")
            print(f"Итерации: {factorial(n)}")
            
        elif ch == "3":
            n = int(input())
            print(f"Рекурсия: {fibo_recursive(n)}")
            print(f"Итерации: {fibo(n)}")
            
        elif ch == "4":
            stack = Stack()
            while True:
                print(f"Стек: {stack.items}")
                print("push/peek/pop/is_empty/min/len/exit")
                cmd = input()
                
                if cmd.startswith("push"):
                    item = int(cmd.split()[1])
                    stack.push(item)
                elif cmd == "pop":
                    try:
                        print(f"Удален: {stack.pop()}")
                    except Exception as e:
                        print(e)
                elif cmd == "peek":
                    try:
                        print(f"Верхний: {stack.peek()}")
                    except Exception as e:
                        print(e)
                elif cmd == "is_empty":
                    print(f"Пустой: {stack.is_empty()}")
                elif cmd == "len":
                    print(f"Длина: {len(stack)}")
                elif cmd == "min":
                    try:
                        print(f"Минимальный: {stack.min()}")
                    except Exception as e:
                        print(e)
                elif cmd == "exit":
                    break
                else:
                    print("Нет команды")
                    
        elif ch == "5":
            queue = Queue()
            while True:
                print(f"Очередь: {queue.items}")
                print("enqueue/dequeue/front/is_empty/len/exit")
                cmd = input()
                
                if cmd.startswith("enqueue"):
                    item = cmd.split()[1]
                    queue.enqueue(item)
                elif cmd == "dequeue":
                    try:
                        print(f"Удален: {queue.dequeue()}")
                    except Exception as e:
                        print(e)
                elif cmd == "front":
                    try:
                        print(f"Первый: {queue.front()}")
                    except Exception as e:
                        print(e)
                elif cmd == "is_empty":
                    print(f"Пустая: {queue.is_empty()}")
                elif cmd == "len":
                    print(f"Размер: {queue.size()}")
                elif cmd == "exit":
                    break
                else:
                    print("Нет команды")
                    
            break
        elif ch == '0':
            break

if __name__ == "__main__":
    main()