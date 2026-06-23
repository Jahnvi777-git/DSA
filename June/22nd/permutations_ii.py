# link: https://leetcode.com/problems/permutations-ii/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        n = len(nums)
        used = [False]*n
        self.f(0, nums, [], used, n)
        res = []
        print(self.ans)
        for x in self.ans:
            if x not in res: res.append(x)
        return res
    
    def f(self, i, nums, p, used, n):
        if len(p) == n:
            self.ans.append(p)
            p = []
            return
        for idx in range(0, n):
            if not used[idx]:
                used[idx] = True
                self.f(idx+1, nums, p+[nums[idx]], used, n)
                used[idx] = False
    
