class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """
        Конструктор класса Queue
        """
        self.data = ''
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is not None:
            self.tail.next_node = Node(data, self.tail.next_node)
            self.tail = self.tail.next_node
            return
        else:
            self.head = Node(data, None)
            self.tail = self.head
            return

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next_node
            return data

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        else:
            current = self.head
            string = ''
            while current is not None:
                string += f'{current.data}'
                if current.next_node != None:
                    string += '\n'
                current = current.next_node
            return string