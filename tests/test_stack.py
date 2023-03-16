"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node,Stack

@pytest.fixture
def node_1_none():
    return Node(1,None)

def test_node_1(node_1_none):
    assert node_1_none.data == 1

def test_node_none(node_1_none):
    assert node_1_none.next_node == None

@pytest.fixture
def stack_zero():
    return Stack()

def test_stack_empty(stack_zero):
    assert stack_zero.push('1') == None

def test_stack_top(stack_zero):
    stack_zero.push('1')
    stack_zero.push('2')
    stack_zero.push('3')
    assert stack_zero.top.data == '3'

def test_stack_next_node(stack_zero):
    stack_zero.push('1')
    stack_zero.push('2')
    stack_zero.push('3')
    assert stack_zero.top.next_node.data == '2'

def test_stack_pop(stack_zero):
    stack_zero.push('1')
    stack_zero.push('2')
    stack_zero.push('3')
    stack_zero.pop()
    stack_zero.pop()
    assert stack_zero.pop() == '1'
    stack_zero.pop()
    assert stack_zero.pop() == None
