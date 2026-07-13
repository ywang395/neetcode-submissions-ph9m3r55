# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue: 
            lvl = []
            for i in range(len(queue)): 
                parent = queue.popleft()
                if parent: 
                    lvl.append(parent.val)
                    queue.append(parent.left)
                    queue.append(parent.right)
            if lvl: 
                res.append(lvl.pop())
        return res