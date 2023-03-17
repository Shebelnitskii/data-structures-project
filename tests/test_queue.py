import pytest
from src.queue import Queue,Node

@pytest.fixture
def node_1_none():
    return Node(1,None)

def test_node_1(node_1_none):
    assert node_1_none.data == 1

def test_node_none(node_1_none):
    assert node_1_none.next_node == None

@pytest.fixture
def queue_zero():
    return Queue()

def test_queue_empty(queue_zero):
    assert queue_zero.data == ''

def test_queue_tail(queue_zero):
    queue_zero.enqueue('1')
    queue_zero.enqueue('2')
    queue_zero.enqueue('3')
    assert queue_zero.tail.data == '3'

def test_queue_head(queue_zero):
    queue_zero.enqueue('1')
    queue_zero.enqueue('2')
    queue_zero.enqueue('3')
    assert queue_zero.head.data == '1'

def test_queue_dequeue(queue_zero):
    queue_zero.enqueue('1')
    queue_zero.enqueue('2')
    queue_zero.enqueue('3')
    queue_zero.dequeue()
    queue_zero.dequeue()
    assert queue_zero.dequeue() == '3'
    queue_zero.dequeue()
    assert queue_zero.dequeue() == None

def test_queue_str(queue_zero):
    assert str(queue_zero) == ''
    queue_zero.enqueue('1')
    queue_zero.enqueue('2')
    queue_zero.enqueue('3')
    assert str(queue_zero) == '1\n2\n3'
