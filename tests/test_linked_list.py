"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

from src.linked_list import Node, LinkedList


def test_node_creation():
    data = {"id": 1}
    node = Node(data)
    assert node.data == data
    assert node.next_node is None


def test_linked_list_insert_beginning():
    ll = LinkedList()
    ll.insert_beginning({"id": 1})
    assert str(ll) == "{'id': 1} -> None"
    ll.insert_beginning({"id": 0})
    assert str(ll) == "{'id': 0} -> {'id': 1} -> None"


def test_linked_list_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end({"id": 1})
    assert str(ll) == "{'id': 1} -> None"
    ll.insert_at_end({"id": 2})
    assert str(ll) == "{'id': 1} -> {'id': 2} -> None"


def test_linked_list_insert_beginning_and_end():
    ll = LinkedList()
    ll.insert_beginning({"id": 1})
    ll.insert_at_end({"id": 2})
    assert str(ll) == "{'id': 1} -> {'id': 2} -> None"


def test_linked_list_str_empty():
    ll = LinkedList()
    assert str(ll) == "None"


def test_linked_list_str_non_empty():
    ll = LinkedList()
    ll.insert_beginning({"id": 1})
    ll.insert_at_end({"id": 2})
    ll.insert_at_end({"id": 3})
    assert str(ll) == "{'id': 1} -> {'id': 2} -> {'id': 3} -> None"