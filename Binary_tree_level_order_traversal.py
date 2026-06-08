from collections import deque
# Defination of a binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        # Initialize the base case
        if not root:
            return []
        # Inityialize the empty result, where we store our result
        result = []

        # Initialize the queue with root 
        queue = deque([root])

        # Process level by level
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # Add left child
                if node.left:
                    queue.append(node.left)

                # Add right child
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
    
# Example Usages
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(root))

    