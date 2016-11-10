#!/usr/bin/env python
import pytest
from lib import Node


def solution(L):
    prev = None
    for n in L:
        if n.next is None:
            break
        else:
            prev = n

    if prev is None:
        return L.d
    else:
        return prev.d


L0 = Node(1)

L1 = Node(1)
[L1.append(x) for x in [1]]

L2 = Node(1)
[L2.append(x) for x in [2]]

L3 = Node(2)
[L3.append(x) for x in [1, 1, 2, 3, 5, 4]]


@pytest.mark.parametrize("L, expected", [
    (L0, 1),
    (L1, 1),
    (L2, 1),
    (L3, 5),
])
def test_solution(L, expected):
    assert expected == solution(L)
