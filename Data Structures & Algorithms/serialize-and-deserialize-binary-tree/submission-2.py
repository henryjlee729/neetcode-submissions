# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []
        self.dfsSerialize(root)
        return ','.join(self.result)
    
    # Helper function for serialize()
    def dfsSerialize(self, node):
        if not node:
            self.result.append('X')
            return

        self.result.append(str(node.val))
        self.dfsSerialize(node.left)
        self.dfsSerialize(node.right)

    # Decodes the encoded data to a tree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.values = data.split(',')
        self.position = 0
        return self.dfsDeserialize()
    
    # Helper function for deserialize()
    def dfsDeserialize(self):
        value = self.values[self.position]
        self.position += 1
        if value == "X":
            return None

        node = TreeNode(int(value))
        node.left = self.dfsDeserialize()
        node.right = self.dfsDeserialize()
        return node