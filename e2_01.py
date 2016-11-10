#!/usr/bin/env python
import pytest
from lib import Node


def solution1(L):
    elm = set()
    prev = None
    for n in L:
        if n.d not in elm:
            elm.add(n.d)
            prev = n
        else:
            prev.next = n.next
    return L


def solution(L):
    def remove_dup(L):
        flag = False
        first = L
        while first is not None:
            prev = first
            n = first.next
            while n is not None:
                if n.d == first.d:
                    print('==', first.d, n.d)
                    try:
                        prev.next = n.next
                    except Exception as e:
                        print('EXCEPTION', first, n, prev)
                        raise e
                else:
                    print('!=', first.d, n.d)
                    prev = n
                n = n.next

            first = first.next

    while remove_dup(L):
        pass
    return L


L0 = Node(1)

L1 = Node(1)
[L1.append(x) for x in [1]]
L1E = Node(1)

L2 = Node(1)
[L2.append(x) for x in [2]]

L3 = Node(1)
[L3.append(x) for x in [2, 1, 2, 3, 1, 4]]

L3E = Node(1)
[L3E.append(x) for x in [2, 3, 4]]


@pytest.mark.parametrize("L, expected", [
    (L0, L0),
    (L1, L1E),
    (L2, L2),
    (L3, L3E),
])
def test_solution(L, expected):
    assert expected == solution1(L) == solution(L)
