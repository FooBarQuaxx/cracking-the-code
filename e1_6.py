#!/usr/bin/env python
import pytest


def solution(M, N):
    res = [[] for _ in range(N)]
    for i in range(N):
            res[i] = [M[j][N-i-1] for j in range(N)]
    return res


M20 = [
        [0, 0],
        [0, 0],
]

M21 = [
        [1, 0],
        [0, 0],
]

M21E = [
        [0, 0],
        [1, 0],
]

M30 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
]

M31 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
]

M31E = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
]

M32 = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0],
]

M32E = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
]

M33 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
]

M33E = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
]

M34 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
]

M35 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
]

M35E = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7],
]


@pytest.mark.parametrize("M, N, expected", [
    (M20, 2, M20),
    (M30, 3, M30),

    (M21, 2, M21E),

    (M31, 3, M31E),
    (M32, 3, M32E),
    (M33, 3, M33E),
    (M34, 3, M34),
    (M35, 3, M35E),
])
def test_solution(M, N, expected):
    assert expected == solution(M, N)
