# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        if root: 
            stack=[root]
        while stack: 
            current = stack.pop()

            if self.isSameTree(current,subRoot):
                return True 
            if current.left: 
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return False

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: 
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)