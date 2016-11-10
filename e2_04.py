#!/usr/bin/env python
import pytest
from lib import Node


def solution(L1, L2):
    n = L = None
    prev = None
    val = 0
    carry = 0
    for n1, n2 in zip(L1, L2):
        sum = n1.d + n2.d + carry
        val = sum % 10
        carry = sum // 10
        new_node = Node(val)
        if L is None:
            L = new_node
        else:
            prev.next = new_node
        prev = new_node

    if carry != 0:
        prev.next = Node(carry)

    return L


L01 = Node.from_list([1])
L02 = Node.from_list([1])
L0E = Node.from_list([2])

L11 = Node.from_list([5])
L12 = Node.from_list([5])
L1E = Node.from_list([0, 1])

L21 = Node.from_list([3, 1, 5])
L22 = Node.from_list([5, 9, 2])
L2E = Node.from_list([8, 0, 8])

L31 = Node.from_list([3, 1, 2])
L32 = Node.from_list([5, 9, 9])
L3E = Node.from_list([8, 0, 2, 1])


@pytest.mark.parametrize("L1, L2, expected", [
    (L01, L02, L0E),
    (L11, L12, L1E),
    (L21, L22, L2E),
    (L31, L32, L3E),
])
def test_solution(L1, L2, expected):
    assert expected == solution(L1, L2)
