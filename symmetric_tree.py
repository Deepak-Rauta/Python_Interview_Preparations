# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def IsSymmetric(self, root):
#         # Helper function to check symmetric
#         def isMirror(t1, t2):
#             if not t1 and not t2:
#                 return True
#             if not t1 or not t2:
#                 return False
#             return (t1.val==t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
#         return isMirror(root.left, root.right) if root else True
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

# solution = Solution()
# print(solution.IsSymmetric(root))


# Definition of a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # The main function, it receive only one tree(root)
    def isSymmetric(self, root):
        # Now, create the helper function
        # Here, we create helper function because during recusrion we need to compare two node at the same time 
        # One node is from the left subtree and one node is from the right subtree
        def isMirror(left, right):
            # Now check if both node are None
            if not left and not right:
                return True
            
            # Now, check if one of them value if empty and one value is difefrent from others
            if not left or not right or left.val != right.val:
                return False
            
            # Compared mirror subtree
            return isMirror(left.left, right.right) and \
                    isMirror(left.right, right.left)
        
        # Now, return the main logic
        return isMirror(root.left, root.right)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))