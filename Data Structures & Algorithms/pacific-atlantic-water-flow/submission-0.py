class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        for row in range(0, len(heights)):
            self.dfs(row, 0, pacific, heights)
            self.dfs(row, len(heights[0]) - 1, atlantic, heights)
        
        for col in range(0, len(heights[0])):
            self.dfs(0, col, pacific, heights)
            self.dfs(len(heights) - 1, col, atlantic, heights)
            
        result = []
        for row in range(0, len(heights)):
            for col in range(0, len(heights[0])):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append((row, col))

        return result

    def dfs(self, row, col, visited, heights):
        if row < 0 or col < 0:
            return
        if row == len(heights) or col == len(heights[0]):
            return
        if (row, col) in visited:
            return

        visited.add((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for ((dr, dc)) in directions:
            newRow = row + dr
            newCol = col + dc
            if newRow < 0 or newCol < 0:
                continue
            if newRow == len(heights) or newCol == len(heights[0]):
                continue
            if (newRow, newCol) in visited:
                continue
            if heights[newRow][newCol] < heights[row][col]:
                continue

            self.dfs(newRow, newCol, visited, heights)