# link: https://leetcode.com/problems/binary-tree-paths/?envType=problem-list-v2&envId=d5qblqpi
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        self.ans = []
        self.f(root, "")
        return self.ans
    
    def f(self, root, path):
        if not root: return
        if not root.left and not root.right:
            path += str(root.val)
            self.ans.append(path)
            return
        if root.left:
            self.f(root.left, path + str(root.val) + '->')
        if root.right:
            self.f(root.right, path + str(root.val) + '->')
