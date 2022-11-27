class Solution:
    def __init__(self, grid: list[list[int]]):
        self._grid_size = len(grid)
        self._grid = grid

    def shortestBridge(self, grid: list[list[int]]) -> int:
        ...

    def _find_island(
        self, list_points: list[list[int]], points_island: list[list[int]]
    ) -> bool:
        for row, col in list_points:
            if [row, col] in points_island:
                print(
                    f"Known land: [{row}, {col}] is already part of island ..."
                )
                pass
            elif self._grid[row][col] == 0:
                print(f"Found water at [{row}, {col}] ...")
            else:
                print(f"Unknown land at [{row}, {col}]...")
                points_island.append([row, col])
                neighbours = self._neighbours(row, col)
                print(f"Neighbours: {neighbours} ...")
                self._find_island(neighbours, points_island)
        return True

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
