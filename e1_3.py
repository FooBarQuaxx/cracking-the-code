#!/usr/bin/env python
import pytest


def solution(S):
    i = 0
    while i < len(S):
        x = S[i]
        j = i + 1
        while j < len(S):
            y = S[j]
            if x == y:
                S = ''.join(S[:j] + S[j+1:])
            else:
                j += 1
        i += 1
    return S


@pytest.mark.parametrize("S, expected", [

    ('',      ''),
    ('a',     'a'),
    ('aa',    'a'),
    ('ab',    'ab'),
    ('abba',  'ab'),
    ('baba',  'ba'),
    ('abbddcc',  'abdc'),
    ('aaabbbdddcccaabbccddabcde',  'abdce'),
    ('abbbbbbaaadddaaccd',  'abdc'),
])
def test_solution(S, expected):
    assert expected == solution(S)
