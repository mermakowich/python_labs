"""
Реализация базовых структур данных: Stack и Queue

Stack - стек (LIFO - Last In, First Out)
Queue - очередь (FIFO - First In, First Out)
"""

from typing import Any
from collections import deque


class Stack:
    """
    Стек (LIFO - Last In, First Out)

    Реализован на основе list, где вершина стека - последний элемент списка

    Все операции выполняются за O(1)
    """

    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """
        Добавляет элемент на вершину стека

        Параметры:
        item - элемент для добавления
        """
        self._data.append(item)

    def pop(self) -> Any:
        """
        Снимает и возвращает верхний элемент стека

        Возвращает:
        верхний элемент стека

        Поднимаем ошибки:
        IndexError - если стек пустой
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """
        Смотрим верхний элемент без удаления

        Возвращает:
        верхний элемент или None, если стек пустой
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """
        Проверяет, пустой ли стек

        Возвращает:
        True если стек пустой, иначе False
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке
        """
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    """
    Очередь (FIFO - First In, First Out)

    Реализована на основе collections.deque
    Голова очереди - левый край, dequeue берёт элементы слева.
    Все операции выполняются за O(1)
    """

    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """
        Добавляет элемент в конец очереди

        Параметры:
        item - элемент для добавления
        """
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Удаляет и возвращает элемент из начала очереди

        Возвращает:
        первый элемент очереди

        Поднимаем ошибки:
        IndexError - если очередь пустая
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """
        Смотрим первый элемент без удаления

        Возвращает:
        первый элемент или None, если очередь пустая
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """
        Проверяет, пустая ли очередь

        Возвращает:
        True если очередь пустая, иначе False
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди
        """
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"


def main():
    """
    Демонстрация работы Stack и Queue
    """

    print("Демонстрация Stack")

    stack = Stack()
    print(f"Создан пустой стек: {stack}")
    print(f"Пустой ли стек? {stack.is_empty()}")

    print("\nДобавляем элементы: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Размер стека: {len(stack)}")

    print(f"\nПросмотр вершины (peek): {stack.peek()}")
    print(f"Извлекаем (pop): {stack.pop()}")
    print(f"Стек после pop: {stack}")

    print(f"Извлекаем (pop): {stack.pop()}")
    print(f"Извлекаем (pop): {stack.pop()}")
    print(f"Стек: {stack}")
    print(f"Пустой ли стек? {stack.is_empty()}")

    print("\nДемонстрация Queue")

    queue = Queue()
    print(f"Создана пустая очередь: {queue}")
    print(f"Пустая ли очередь? {queue.is_empty()}")

    print("\nДобавляем элементы: A, B, C")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"Очередь: {queue}")
    print(f"Размер очереди: {len(queue)}")

    print(f"\nПросмотр первого (peek): {queue.peek()}")
    print(f"Извлекаем (dequeue): {queue.dequeue()}")
    print(f"Очередь после dequeue: {queue}")

    print(f"Извлекаем (dequeue): {queue.dequeue()}")
    print(f"Извлекаем (dequeue): {queue.dequeue()}")
    print(f"Очередь: {queue}")
    print(f"Пустая ли очередь? {queue.is_empty()}")


if __name__ == "__main__":
    main()
