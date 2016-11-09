#!/usr/bin/env python
import pytest


def solution1(S):
    return len(set(S)) == len(S)


def solution(S):
    s = sorted(S)
    for i in range(0, len(S) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


@pytest.mark.parametrize("S, expected", [
    ('',     True),
    ('a',    True),
    ('abc',  True),
    ('aa',   False),
    ('aba',  False),
    ('cabcda', False),
])
def test_solution(S, expected):
    assert expected == solution(S)
