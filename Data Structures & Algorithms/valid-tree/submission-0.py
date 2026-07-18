class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = []
        for i in range(0, n):
            adjacency.append([])
        for (u, v) in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        visited = set()
        if not self.dfs(0, -1, visited, adjacency):
            return False
        if len(visited) != n:
            return False
       
        return True

    def dfs(self, node, parent, visited, adjacency):
        if node in visited:
            return False
        
        visited.add(node)
        for neighbor in adjacency[node]:
            if neighbor == parent:
                continue
            if not self.dfs(neighbor, node, visited, adjacency):
                return False

        return True