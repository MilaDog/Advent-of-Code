import heapq as hq
import itertools
from collections import defaultdict
from copy import deepcopy
from timeit import timeit

from src.common.python.timing import Timing


class Solution:
    """Solutions to the problems."""

    def __init__(self, data: list[tuple[int, int]]) -> None:
        self.byte_positions: list[tuple[int, int]] = data
        self.directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.size: tuple[int, int] = (70, 70)
        self.number_bytes: int = 1024
        self.start: tuple[int, int] = (0, 0)
        self.end: tuple[int, int] = (70, 70)

    @classmethod
    def parse_input(cls) -> "Solution":
        """Parse the problem data input to be used.

        Returns:
            Solution:
                Class instance with the parsed input data.
        """
        with open("input.txt", "r") as file:
            values: list[tuple[int, int]] = []

            for line in file.readlines():
                x, y = map(int, line.strip().split(","))
                values.append((x, y))

        return cls(data=values)

    def display(self, grid: dict[tuple[int, int], str]) -> None:
        """Display the grid.

        Args:
            grid (dict[tuple[int, int]]):
                Grid to display.

        Returns:
            None
        """
        for x in range(self.size[0] + 1):
            row: list[str] = [grid[(x, y)] for y in range(self.size[1] + 1)]
            print("".join(row))

    def traverse(
        self,
        grid: dict[tuple[int, int], str],
        corrupt_areas: list[tuple[int, int]],
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> set[tuple[int, int]]:
        """Traverse the grid, returning the shortest taken path.

        Args:
            grid (dict[tuple[int, int], str]):
                Grid to traverse.
            corrupt_areas (list[tuple[int, int]]):
                Corrupt areas within the grid.
            start (tuple[int,int]):
                Starting position.
            end (tuple[int, int]):
                Ending position.

        Returns:
            set[tuple[int, int]]:
                Shortest taken path.
        """
        for ca in corrupt_areas:
            grid[ca] = "#"

        pq: list[tuple[int, tuple[int, int], set[tuple[int, int]]]] = [(0, start, {start})]
        visited: set[tuple[int, int]] = set()
        taken_path: set[tuple[int, int]] = set()

        while pq:
            steps, position, path = hq.heappop(pq)
            x, y = position

            if position in visited:
                continue
            visited.add(position)

            if position == end:
                taken_path = path
                break

            for dx, dy in self.directions:
                new_position: tuple[int, int] = (x + dx, y + dy)

                if grid.get(new_position, "#") == "#":
                    continue

                hq.heappush(pq, (steps + 1, new_position, path | {new_position}))

        return taken_path

    def setup_grid(self) -> dict[tuple[int, int], str]:
        """Set up the grid for the problem.

        Returns:
            dict[tuple[int, int], str]:
                Create grid.
        """
        grid: dict[tuple[int, int], str] = defaultdict(str)

        for x, y in itertools.product(range(self.size[0] + 1), range(self.size[1] + 1)):
            grid[(x, y)] = "."

        return grid

    def solve(self) -> None:
        """Solve Part 01 of the problem.

        Returns:
            None
        """
        grid: dict[tuple[int, int], str] = self.setup_grid()
        path_taken: set[tuple[int, int]] = self.traverse(
            grid=deepcopy(grid), corrupt_areas=self.byte_positions[:1024], start=self.start, end=self.end
        )

        print(f"Part 01: {len(path_taken)-1}")

        # Finding the first coordinates that corrupt the path
        low: int
        mid: int
        high: int
        low, high = 1024, len(self.byte_positions)
        mid = 0

        while low != high:
            mid = (low + high) // 2

            if self.traverse(
                grid=deepcopy(grid), corrupt_areas=self.byte_positions[:mid], start=self.start, end=self.end
            ):
                low = mid + 1
            else:
                high = mid

        print(f"Part 02: {",".join(list(map(str, self.byte_positions[mid])))}")


if __name__ == "__main__":
    sol: Solution = Solution.parse_input()

    print(Timing(timeit(sol.solve, number=1)).result(), "\n")
