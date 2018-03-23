# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,root,depth):
        
        if root is None :
            return depth
        
        if not root.left or not root.right :
            return max(self.dfs(root.left,depth+1),self.dfs(root.right,depth+1))
        else :
            return min(self.dfs(root.left,depth+1),self.dfs(root.right,depth+1))
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.dfs(root,0)