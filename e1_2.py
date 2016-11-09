#!/usr/bin/env python
import pytest


def solution(S):
    return ''.join([S[i] for i in range(len(S)-1, -1, -1)])


@pytest.mark.parametrize("S, expected", [
    ('',     ''),
    ('ab',   'ba'),
    ('aba',  'aba'),
    ('abab',  'baba'),
])
def test_solution(S, expected):
    assert expected == solution(S)
