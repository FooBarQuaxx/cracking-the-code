#!/usr/bin/env python
import pytest


def solution(S):
    i = 0
    while i < len(S):
        x = S[i]
        if x == ' ':
            # print("'%s', '%s'" % (S[:i], S[i+1:]))
            S = '%20'.join([S[:i], S[i+1:]])
            i += 2
        else:
            i += 1
    return S


@pytest.mark.parametrize("S, expected", [
    ('', ''),
    (' ', '%20'),
    ('a b', 'a%20b'),
    (' x ', '%20x%20'),
])
def test_solution(S, expected):
    assert expected == solution(S)
