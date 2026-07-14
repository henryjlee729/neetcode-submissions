"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        result = {}
        return self.dfs(node, result)

    def dfs(self, node, result):
        if node in result:
            return result[node]
        
        copyNode = Node(node.val)
        result[node] = copyNode
        for neighbor in node.neighbors:
            newNode = self.dfs(neighbor, result)
            copyNode.neighbors.append(newNode)
       
        return copyNode