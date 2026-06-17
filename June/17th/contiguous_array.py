# link: https://leetcode.com/problems/contiguous-array/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [-1 if i == 0 else 1 for i in nums]
        ps = {0: -1}
        t = 0
        ans = 0
        for i in range(len(a)):
            t += a[i]
            if t not in ps: ps[t] = i
            else: ans = max(ans, i - ps[t])
        return ans 
         