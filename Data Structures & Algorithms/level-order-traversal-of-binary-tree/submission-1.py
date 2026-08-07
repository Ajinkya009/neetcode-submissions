# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        level_order = defaultdict(list)
        def dfs(node,level,level_order):
            if node:
                level_order[level].append(node.val)
                if node.left:
                    dfs(node.left,level+1,level_order)
                if node.right:
                    dfs(node.right,level+1,level_order)
            return
        dfs(root,0,level_order)
        return list(level_order.values())

