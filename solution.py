# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        found = None
        if root == None:
            return
        else: 
            if root.val == val:
                return root
            else:
                tmp = self.searchBST(root.right, val)
                if  tmp != None:
                    found = tmp
                tmp = self.searchBST(root.left, val)
                if tmp != None:
                    found = tmp
                    
        return found
