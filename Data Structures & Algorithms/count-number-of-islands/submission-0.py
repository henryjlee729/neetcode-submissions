class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    self.dfs(row, col, grid)

        return islands

    def dfs(self, row, col, grid):
        if row < 0 or col < 0:
            return
        if row == len(grid) or col == len(grid[0]):
            return
        if grid[row][col] == "0":
            return
        
        grid[row][col] = "0"
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)