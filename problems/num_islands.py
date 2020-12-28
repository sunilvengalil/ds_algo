# https://leetcode.com/submissions/detail/432485095/

def get_neighbour_indices(i, j, m, n):
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < m - 1:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < n - 1:
        neighbours.append((i, j + 1))
    return neighbours


class Solution(object):

    def find_connected_ones(self, i, j):
        self.visited[i][j] = 1
        neighbour_indices = get_neighbour_indices(i, j, self.m, self.n)
        for neighbour_index in neighbour_indices:
            if self.grid[neighbour_index[0]][neighbour_index[1]] == "0":
                continue
            if self.visited[neighbour_index[0]][neighbour_index[1]] == 1:
                continue
            self.find_connected_ones(neighbour_index[0], neighbour_index[1])

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        self.m = len(grid)
        if len(grid[0]) == 0:
            return 0
        self.n = len(grid[0])
        self.grid = grid
        self.visited = [[0] * self.n for i in range(self.m)]
        # print(visited)
        num_islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.visited[i][j]:
                    continue
                if grid[i][j] == "0":
                    continue
                self.visited[i][j] = 1
                num_islands += 1
                # grid[i][j] is "1". find the connected components
                self.find_connected_ones(i, j)
        return num_islands