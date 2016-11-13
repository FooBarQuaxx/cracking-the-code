#!/usr/bin/env python
import pytest
from lib import Stack


class StackSet(object):


    def __init__(self, stack_max_size, elements=[]):

        self._stacks = []
        self._stack_max_size = stack_max_size
        def chunck(l):
            n = 0
            l_len = len(l)
            while n < l_len:
                yield slice(n, min(n+stack_max_size, l_len), 1)
                n += stack_max_size
        for sl in chunck(elements):
            self._stacks.append(Stack(elements[sl]))


    def __len__(self):
        return sum([len(s) for s in self._stacks])

    def push(self, value):
        if self.stacks_num == 0:
            self._stacks = [Stack([value])]
        else:
            top_stack = self._stacks[-1]
            if top_stack.size == self._stack_max_size:
                self._stacks.append(Stack([value]))
            else:
                top_stack.push(value)


    def pop(self):
        if self.stacks_num == 0:
            return None
        top_stack = self._stacks[-1]
        value = top_stack.pop()
        if top_stack.size == 0:
            self._stacks.pop()
        return value

    @property
    def size(self):
        return len(self)

    @property
    def stacks_num(self):
        return len(self._stacks)

    @property
    def stack_max_size(self):
        return self._stack_max_size


def test_create_stack_set():
    s = StackSet(1)
    assert s.size == 0
    assert s.stacks_num == 0

    s = StackSet(2, [1,2])
    assert s.size == 2
    assert s.stacks_num == 1

    s = StackSet(5, [x for x in range(10)])
    assert s.size == 10
    assert s.stacks_num == 2

    s = StackSet(5, [x for x in range(11)])
    assert s.size == 11
    assert s.stacks_num == 3

def test_stack_set_push():
    s = StackSet(5, [x for x in range(9)])
    assert s.stacks_num == 2
    s.push(1)
    assert s.stacks_num == 2

    s.push(1)
    assert s.stacks_num == 3


def test_stack_set_pop():
    s = StackSet(5)
    assert s.pop() is None

    s = StackSet(5, [x for x in range(11)]) #  [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10]
    assert s.stacks_num == 3

    x = s.pop()
    assert x == 10
    assert s.stacks_num == 2
