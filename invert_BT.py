class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        # swap left and right child
        root.left, root.right = root.right, root.left

        # Recursively call left and right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

