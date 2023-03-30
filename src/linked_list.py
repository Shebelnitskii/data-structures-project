class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        node = self.head
        linked_list_data = []
        while node:
            linked_list_data.append(node.data)
            node = node.next_node
        return linked_list_data

    def get_data_by_id(self, id_value) -> dict:
        """Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению"""
        node = self.to_list()
        for item in node:
            try:
                if item['id'] == id_value:
                    return item
            except TypeError:
                print("Ошибка: данные не являются словарём или в словаре нет id.")
