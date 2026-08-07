# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_sided_view = []

        def dfs(node,depth):
            if depth == len(right_sided_view):
                right_sided_view.append(node.val)
            if node.right:
                dfs(node.right,depth+1)
            if node.left:
                dfs(node.left,depth+1)
        
        dfs(root,0)
        return right_sided_view

