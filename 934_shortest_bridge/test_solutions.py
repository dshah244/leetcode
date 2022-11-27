import pytest
from solutions import Solution


@pytest.fixture()
def sample_grid() -> Solution:
    """Return object under test initialized using a grid."""
    grid = [
        [1, 1, 1, 0, 0],  # 0
        [1, 1, 0, 0, 0],  # 1
        [0, 0, 0, 0, 0],  # 2
        [0, 0, 1, 0, 0],  # 3
        [0, 1, 1, 1, 0],  # 4
#        0  1  2  3  4
    ]
    return Solution(grid)


def test_neighbours(sample_grid: Solution):
    """Validate that neighbours to a point are correctly identified."""
    neighbours = sample_grid._neighbours(row=4, col=2)
    assert neighbours == [[4, 1], [3, 2], [4, 3]]
