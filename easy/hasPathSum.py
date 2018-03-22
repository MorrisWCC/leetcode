class Solution:
    def dfs(self,node,sum):

        if node is None :
            return False
        
        sum -= node.val 

        if sum == 0 :
            if node.left is None and node.right is None :
                return True

        return ( self.dfs(node.left,sum) | self.dfs(node.right,sum) )
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,sum)