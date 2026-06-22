# link: https://leetcode.com/problems/construct-string-from-binary-tree/description/?envType=problem-list-v2&envId=d5qblqpi
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if not root: return ""
        s = str(root.val)
        if root.left:
            s += '(' + self.tree2str(root.left) + ')'
        elif root.right:
            s += '()'
        if root.right:
            s += '(' + self.tree2str(root.right) + ')'
        return s 
