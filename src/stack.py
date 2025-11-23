class Stack:
    """
    Stack на list 
    """
    def __init__(self):
        """
        Создание списка для хранения
        """
        self.items = []
    
    def push(self, x: int) -> None:
        """
        Добавляет элемент в виде кортежа
        """
        if self.is_empty():
            self.items.append((x, x))
        else:
            m = min(x, self.items[-1][1])
            self.items.append((x, m))
    
    def pop(self) -> int:
        """
        Удаление элемента из стэка. Метод возвращает удалённый элемент
        """
        if self.is_empty():
            raise Exception("Пустой стэк")
        return self.items.pop()[0]

    def peek(self) -> int:
        """
        Получение последнего элемента
        """
        if self.is_empty():
            raise Exception("Пустой стэк")
        return self.items[-1][0]

    def is_empty(self) -> bool:
        """
        Проверка исключения
        """
        return len(self.items) == 0

    def __len__(self) -> int:
        """
        Получение длины стэка
        """
        return len(self.items)

    def min(self) -> int:
        """
        Получение минимального элемента в стэке
        """
        if self.is_empty():
            raise Exception("Пустой стэк")
        return self.items[-1][1] 