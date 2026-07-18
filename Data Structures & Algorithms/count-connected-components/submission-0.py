class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = []
        for i in range(0, n):
            adjacency.append([])
        for (u, v) in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        components = 0
        visited = set()
        for node in range(0, n):
            if node not in visited:
                components += 1
                self.dfs(node, visited, adjacency)
    
        return components

    def dfs(self, node, visited, adjacency):
        if node in visited:
            return
        
        visited.add(node)
        for neighbor in adjacency[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, adjacency)