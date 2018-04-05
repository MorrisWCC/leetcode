class Solution:
    def fulfill_set(self, my_set, root):
        if root is None :
            return 
        my_set.add(root.val)
        self.fulfill_set(my_set,root.left)
        self.fulfill_set(my_set,root.right)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        my_set = set()
        
        self.fulfill_set( my_set, root )
        
        for num in my_set :
            if (k - num != num) and k - num in my_set :
                return True
        else :
            return False