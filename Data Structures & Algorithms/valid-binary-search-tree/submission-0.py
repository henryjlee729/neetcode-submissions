# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, minVal, maxVal):
        if not node:
            return True
        if node.val < minVal or node.val > maxVal:
            return False

        return self.dfs(node.left, minVal, node.val - 1) and self.dfs(node.right, node.val + 1, maxVal)