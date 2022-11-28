class Solution:
    def __init__(self, grid: list[list[int]]):
        self._grid_size = len(grid)
        self._grid = grid

    def shortestBridge(self, grid: list[list[int]]) -> int:
        ...

    def _find_islands(self) -> list[list[list[int]]]:
        islands = []
        for row, one_row in enumerate(self._grid):
            for col, one_point in enumerate(one_row):
                if [row, col] not in self._list_all_land_points(
                    islands
                ) and one_point == 1:
                    points_island = []
                    _ = self._find_island([[row, col]], points_island)
                    islands.append(points_island)
        return islands

    def _list_all_land_points(self, vector: list[list[list[int]]]):
        reduced = []
        for one_ele in vector:
            reduced += one_ele
        return reduced

    def _find_island(
        self, list_points: list[list[int]], points_island: list[list[int]]
    ) -> bool:
        for row, col in list_points:
            if [row, col] in points_island:
                print(
                    f"Known land: [{row}, {col}] is already part of island ..."
                )
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
        return [] if col == 0 else [row, col - 1]

    def _neighbour_north(self, row: int, col: int) -> list[int]:
        return [] if row == 0 else [row - 1, col]

    def _neighbour_east(self, row: int, col: int) -> list[int]:
        return [] if col == self._grid_size - 1 else [row, col + 1]

    def _neighbour_south(self, row: int, col: int) -> list[int]:
        return [] if row == self._grid_size - 1 else [row + 1, col]

    def distance(self, point_a: list[int], point_b: list[int]) -> int:
        return abs(sum(point_a) - sum(point_b))
