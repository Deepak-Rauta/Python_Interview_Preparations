"""At first glance, Minimum Depth of Binary Tree seems like it should be the exact same logic, just swapping out the max() function for min(). So your formula would look like: depth = 1 + min(left_depth, right_depth).
But there is a classic "gotcha" in this problem!

The Gotcha: Skewed Trees
By definition, the minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. A leaf node is a node that has zero children.

Imagine a tree where the root has a right child, but no left child.
If you just use min(left_depth, right_depth), the left side will return 0 (because it's empty).

Your formula will calculate 1 + 0 = 1.
But wait! The root isn't a leaf node because it still has a right child.

The Updated Logic
To fix this, we have to force the code to ignore empty branches and only calculate the depth of branches that actually lead to a leaf.

Here is how you adjust your thinking for this one:
Base Case: If the node is empty, return 0.
Left is Empty: If there is no left child, you must go right. Return 1 + right_depth.

Right is Empty: If there is no right child, you must go left. Return 1 + left_depth.

Both Exist: If the node has both children, now you can use your formula: 1 + min(left_depth, right_depth)."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        # 1. Base Case: if the tree is empty
        if root is None:
            return 0
        
        # 2. Left is empty we must go right to find the leaf
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # 3. Right is empty we must go left to find the leaf
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist: Now we can safely use the min() function
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Example Usages
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

solution_instance = Solution()
print(solution_instance.minDepth(root))
