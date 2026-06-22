# link:https://leetcode.com/problems/path-sum-ii/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):

    def pathSum(self, root, targetSum):
        self.ans = []
        self.f(root, [], 0, targetSum)
        return self.ans

    def f(self, root, path, s, target):
        if not root:
            return
        path = path + [root.val]
        s += root.val
        if not root.left and not root.right:
            if s == target:
                self.ans.append(path)
            return
        self.f(root.left, path, s, target)
        self.f(root.right, path, s, target)
