class Solution:
    def __init__(self, grid: list[list[int]]):
        self._grid_size = len(grid)

    def shortestBridge(self, grid: list[list[int]]) -> int:
        self._grid = grid

    def _find_island(list_points: list[list[int]]) -> list[list[int]]:
        ...

    def _neighbours(self, row: int, col: int) -> list[list[int]]:
        return [
            one_point
            for one_point in [
                self._neighbour_west(row, col),
                self._neighbour_north(row, col),
                self._neighbour_east(row, col),
                self._neighbour_south(row, col),
            ]
            if one_point
        ]

    def _neighbour_west(self, row: int, col: int) -> list[int]:
        if col == 0:
            return []
        return [row, col - 1]

    def _neighbour_north(self, row: int, col: int) -> list[int]:
        if row == 0:
            return []
        return [row - 1, col]

    def _neighbour_east(self, row: int, col: int) -> list[int]:
        if col == self._grid_size - 1:
            return []
        return [row, col + 1]

    def _neighbour_south(self, row: int, col: int) -> list[int]:
        if row == self._grid_size - 1:
            return []
        return [row + 1, col]

    def distance(point_a: list[int], point_b: list[int]) -> int:
        return abs(sum(point_a) - sum(point_b))
