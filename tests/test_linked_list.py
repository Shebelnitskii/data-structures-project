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

def test_to_list():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    assert ll.to_list() == [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'}]

def test_get_data_by_id():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    assert ll.get_data_by_id(3) == {'id': 3, 'username': 'mosh_s'}
    assert ll.get_data_by_id(5) is None
    assert ll.get_data_by_id('id_value') is None

def test_get_data_by_error():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    assert ll.get_data_by_id(3) == None