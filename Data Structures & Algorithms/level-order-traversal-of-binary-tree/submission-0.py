# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append (root)
        result=[]
        while queue : 
            children = []
            for i in range(len(queue)):
                parent = queue.popleft()
                if parent : 
                    children.append(parent.val)
                    queue.append(parent.left)
                    queue.append(parent.right)
            if children: 
                result.append(children)
        return result