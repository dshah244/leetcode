class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        self._grid = grid

    def _find_island(list_points: list[list[int]]) -> list[list[int]]:
        ...

    def _neighbours(self, one_point: list[int]) -> list[list[int]]:
        ...

    def _neighbour_west(self, one_point: list[int]) -> int:
        ...

    def _neighbour_north(self, one_point: list[int]) -> int:
        ...

    def _neighbour_east(self, one_point: list[int]) -> int:
        ...

    def _neighbour_south(self, one_point: list[int]) -> int:
        ...

    def distance(point_a: list[int], point_b: list[int]) -> int:
        return abs(sum(point_a) - sum(point_b))
