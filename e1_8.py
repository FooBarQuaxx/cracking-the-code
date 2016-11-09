#!/usr/bin/env python
import pytest


def isSubstring(s1, s2):
    return s1.find(s2) != -1


def solution(S1, S2, i=0):
    if len(S1) != len(S2):
        return False
    return isSubstring(S2 * 2, S1)


@pytest.mark.parametrize("S1, S2, expected", [

    ('',               '',             True),
    ('a',              'a',            True),
    ('aa',             'aa',           True),
    ('aaa',            'aa',           False),
    ('ab',           'ba',           True),
    ('waterbottle',  'erbottlewat',  True)
])
def test_solution(S1, S2, expected):
    assert expected == solution(S1, S2)
