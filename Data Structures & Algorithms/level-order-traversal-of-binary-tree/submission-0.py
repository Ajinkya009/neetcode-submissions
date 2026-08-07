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
        level_order = []

        q = deque([root])

        while q:
            q_len = len(q)
            order = []
            while q_len:
                node = q.popleft()
                order.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                q_len-=1
            level_order.append(order)
        return level_order