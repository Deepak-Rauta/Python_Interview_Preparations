# Definition for a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # Base case
        if not root:
            return 0
        
        # Find the left subtree depth
        left_depth = self.maxDepth(root.left)

        # Find the right subtree depth
        right_depth = self.maxDepth(root.right)

        # Return current depth
        return 1 + max(left_depth, right_depth)
    
# Example Usages
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

solution_instance = Solution()
print(solution_instance.maxDepth(root))


# Important points to remember:-
# 01. def maxDepth(node) means what is the depth starting from this node
# 02. For every node the formula is:- depth = 1 + max(left_depth, right_depth)
# 03. Each node ask its childeren what is your depth? then choose the bigger deoth and add itself.
# The Time and Space Complexity
# Time Complexity is:- O(n) Bcz each node is visited once
# SpaCE cOMPLEXITY IS:- o(h) where h = height of the tree (recurssion stack)    