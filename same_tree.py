class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubTree(self, p, q):
        if not p and not q:
            return True
    # if one of them value is empty or there value is different from each other
        if not p or not q or p.val != q.val:
            return False
        return self.isSubTree(p.left, q.left) and self.isSubTree(p.right, q.right)
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

solution_instance = Solution()
print(solution_instance.isSubTree(p, q))