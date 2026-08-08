# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        max_so_far = root.val

        def dfs(node,max_so_far):
            if not node:
                return 0
            total = 0
            if node.val>=max_so_far:
                total+=1
                max_so_far = node.val
            total+=dfs(node.left,max_so_far)
            total+=dfs(node.right,max_so_far)
            return total
        
        return dfs(root,max_so_far)