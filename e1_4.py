#!/usr/bin/env python
import pytest
from collections import Counter


def solution(S1, S2):
    return Counter(S1) == Counter(S2)


@pytest.mark.parametrize("S1, S2, expected", [

    ('',      '',      True),
    ('abc',   'abc',   True),
    ('abc',   'bac',   True),
    ('abc',   'cab',   True),
    ('cafe',  'face',  True),
    ('abbc',  'abc',  False),
    ('abca',  'abc',  False),
    ('a',     'b',    False),
])
def test_solution(S1, S2, expected):
    assert expected == solution(S1, S2)
