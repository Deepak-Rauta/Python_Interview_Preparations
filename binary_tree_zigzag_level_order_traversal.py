from collections import deque

# Defination for a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        # Initialize the base case
        if not root:
            return []
        
        # Initialize the empty result, in where we can store our result
        result = []

        # Initialize the queue with root
        queue = deque([root])

        # Maintain a flag
        left_to_right = True

        # Process level-by-level
        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                # Adding left child
                if node.left:
                    queue.append(node.left)

                # Adding right child
                if node.right:
                    queue.append(node.right)

            # Reverse every alternate level
            if not left_to_right:
                level.reverse()

            result.append(level)

            # Now, toggle the direction
            left_to_right = not left_to_right

        # return the result
        return result
    
# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.zigzagLevelOrder(root))
