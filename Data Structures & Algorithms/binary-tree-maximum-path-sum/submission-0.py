# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.dfs(root)
        return self.maxSum

    def dfs(self, node):
        if not node:
            return 0

        leftPath = max(self.dfs(node.left), 0)
        rightPath = max(self.dfs(node.right), 0)
        path = node.val + leftPath + rightPath

        self.maxSum = max(self.maxSum, path)
        return node.val + max(leftPath, rightPath)        