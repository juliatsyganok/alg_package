class Queue:
    """
    Queue на list
    """
    def __init__(self):
        """
        Создание списка для хранения
        """
        self.items = []
    
    def enqueue(self, x: int) -> None:
        """
        Добавление элемента
        """
        self.items.append(x)
    
    def dequeue(self) -> int:
        """
        Удаляет элемента. Метод возвращает удалённый элемент
        """
        if self.is_empty():
            raise Exception("Пустая очередь")  
        return self.items.pop(0)
    
    def front(self) -> int:
        """
        Получение первого элемента
        """
        if self.is_empty():
            raise Exception("Пустая очередь") 
        return self.items[0] 
    
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
