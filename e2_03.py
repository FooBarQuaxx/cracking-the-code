#!/usr/bin/env python
import pytest
from lib import Node


def solution(L, E):
    prev = None
    for n in L:
        if n.d == E:
            if prev is None:
                L = L.next
            else:
                prev.next = n.next
            break
        prev = n
    return L


L0 = Node.from_list([1])

L1 = Node.from_list([1, 1])
L1E = Node.from_list([1])

L2 = Node.from_list([1, 2, 3, 4])
L2E = Node.from_list([1, 3, 4])

L3 = Node.from_list([1, 2, 3])
L3E = Node.from_list([1, 2])


@pytest.mark.parametrize("L, E, expected", [
    (L0, 0, L0),
    (L1, 1, L1E),
    (L2, 2, L2E),
    (L3, 3, L3E),
])
def test_solution(L, E, expected):
    L = solution(L, E)
    assert L == expected
