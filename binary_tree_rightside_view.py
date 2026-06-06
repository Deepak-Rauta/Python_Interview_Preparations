# The main concept of this code is:-
# BFS + Level order of traversal

from collections import deque
# Definition for a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        # 01. Initialize the base case
        if not root:
            return []
        
        # 02.Initialize an empty result, where we can store my result
        result = []

        # 03. Initialize the queue with root node
        queue = deque([root])

        # 04. Process level by leve
        # If queue is not empty then enter
        while queue:
            level_size = len(queue)

            # 05.Traverse all node of current level
            for i in range(level_size):
                # Here popleft() remove and return the left most element
                node = queue.popleft()

                # 06. Now, check if this is the last node of the level,
                # this is visible for the right side
                if i == level_size - 1:
                    result.append(node.val)

                # 07. Now, check for the left child
                if node.left:
                    queue.append(node.left)

                # 08. Now check for the right child
                if node.right:
                    queue.append(node.right)

        # 09. Return the result
        return result
    
# Example Usages
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.right = TreeNode(4)

obj = Solution()
print(obj.rightSideView(root))
    

