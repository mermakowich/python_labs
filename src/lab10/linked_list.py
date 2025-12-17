"""
Реализация односвязного списка

Односвязный список состоит из узлов, где каждый узел хранит значение и ссылку на следующий узел.
"""

from typing import Any, Iterator


class Node:
    """
    Узел односвязного списка

    Атрибуты:
    value - значение элемента
    next - ссылка на следующий узел или None
    """

    def __init__(self, value: Any, next_node: "Node | None" = None):
        """
        Создаёт новый узел

        Параметры:
        value - значение узла
        next_node - ссылка на следующий узел (по умолчанию None)
        """
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список (Singly Linked List)

    Элементы хранятся в узлах, связанных ссылками.
    Поддерживает операции добавления, вставки, удаления и итерации.
    """

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """
        Добавляет элемент в конец списка

        Сложность: O(1)

        Параметры:
        value - значение для добавления
        """
        new_node = Node(value)

        if self.head is None:
            # Список пустой - новый узел становится и head, и tail
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем в конец
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value: Any) -> None:
        """
        Добавляет элемент в начало списка

        Сложность: O(1)

        Параметры:
        value - значение для добавления
        """
        new_node = Node(value, self.head)
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """
        Вставляет элемент по индексу

        Сложность: O(n) в худшем случае

        Параметры:
        idx - индекс для вставки (0 <= idx <= len(list))
        value - значение для вставки

        Поднимаем ошибки:
        IndexError - если индекс вне допустимого диапазона
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """
        Удаляет элемент по индексу

        Сложность: O(n) в худшем случае

        Параметры:
        idx - индекс элемента для удаления

        Поднимаем ошибки:
        IndexError - если индекс некорректен
        """
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size})")

        if idx == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        node_to_remove = current.next
        current.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = current

        self._size -= 1

    def remove(self, value: Any) -> None:
        """
        Удаляет первое вхождение значения

        Сложность: O(n)

        Параметры:
        value - значение для удаления

        Если значение не найдено, ничего не происходит
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                node_to_remove = current.next
                current.next = node_to_remove.next

                if node_to_remove == self.tail:
                    self.tail = current

                self._size -= 1
                return

            current = current.next

    def __iter__(self) -> Iterator[Any]:
        """
        Возвращает итератор по значениям списка

        Сложность: O(n) для полного обхода
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        elements = list(self)
        return f"SinglyLinkedList({elements})"


def main():
    """
    Демонстрация работы SinglyLinkedList
    """

    print("Демонстрация SinglyLinkedList")

    lst = SinglyLinkedList()
    print(f"Создан пустой список: {lst}")
    print(f"Длина: {len(lst)}")

    print("\nДобавление элементов (append)")
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"После append(1, 2, 3): {lst}")

    print("\nДобавление в начало (prepend)")
    lst.prepend(0)
    print(f"После prepend(0): {lst}")

    print("\nВставка по индексу (insert)")
    lst.insert(2, 1.5)
    print(f"После insert(2, 1.5): {lst}")

    print("\nИтерация по списку")
    print("Элементы:", end=" ")
    for value in lst:
        print(value, end=" ")
    print()

    print("\nУдаление по значению (remove)")
    lst.remove(1.5)
    print(f"После remove(1.5): {lst}")

    print("\nУдаление по индексу (remove_at)")
    lst.remove_at(0)
    print(f"После remove_at(0): {lst}")

    print(f"\nФинальная длина списка: {len(lst)}")


if __name__ == "__main__":
    main()
