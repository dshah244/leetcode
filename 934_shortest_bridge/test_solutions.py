import pytest

from .solutions import Solution


@pytest.fixture()
def grid() -> list[list[int]]:
    return [
        [1, 1, 1, 0, 0],  # 0
        [1, 1, 0, 0, 0],  # 1
        [0, 0, 0, 0, 0],  # 2
        [0, 0, 1, 0, 0],  # 3
        [0, 1, 1, 1, 0],  # 4
        #        0 1 2 3 4
    ]


def test_neighbours(grid: list[list[int]]):
    solution = Solution(grid)
    neighbours = solution._neighbours(row=4, col=2)
    assert neighbours == [[4, 1], [3, 2], [4, 3]]
