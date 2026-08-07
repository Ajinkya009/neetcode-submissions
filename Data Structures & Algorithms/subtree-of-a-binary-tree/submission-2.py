# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_same_tree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.is_same_tree(p.left,q.left) and self.is_same_tree(p.right,q.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        if not root:
            return False

        if self.is_same_tree(root,subroot):
            return True
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
