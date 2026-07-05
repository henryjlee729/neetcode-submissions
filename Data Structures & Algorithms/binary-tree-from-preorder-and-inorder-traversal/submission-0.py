# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        rootValue = preorder[0]
        root = TreeNode(rootValue)
        
        rootIndex = inorder.index(rootValue)
        leftInorder = inorder[:rootIndex]
        rightInorder = inorder[rootIndex + 1:]

        leftSize = len(leftInorder)
        leftPreorder = preorder[1:leftSize + 1]
        rightPreorder = preorder[leftSize + 1:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root