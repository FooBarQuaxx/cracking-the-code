#!/usr/bin/env python
import pytest
import itertools


def solution(M, m, n):
    mutated = set()
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0:
                mutated.update(
                        itertools.chain(
                            zip(itertools.repeat(i, n), range(n)),
                            zip(range(m), itertools.repeat(j, m))
                            )
                        )
    for x, y in mutated:
        M[x][y] = 0

    return M


M220 = [
        [1, 1],
        [1, 1],
]

M221 = [
        [0, 1],
        [1, 1],
]

M221E = [
        [0, 0],
        [0, 1],
]

M231 = [
        [0, 1, 1],
        [1, 1, 1],
]

M231E = [
        [0, 0, 0],
        [0, 1, 1],
]

M232 = [
        [1, 0, 1],
        [1, 1, 1],
]

M232E = [
        [0, 0, 0],
        [1, 0, 1],
]

M341 = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
]

M341E = [
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
]


@pytest.mark.parametrize("M, m, n, expected", [
    (M220, 2, 2, M220),
    (M221, 2, 2, M221E),
    (M231, 2, 3, M231E),
    (M232, 2, 3, M232E),
    (M341, 3, 4, M341E),
])
def test_solution(M, m, n, expected):
    assert expected == solution(M, m, n)
