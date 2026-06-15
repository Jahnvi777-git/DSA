# link: https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        ans = []
        n = len(nums)
        while i < n:
            l = i
            r = i
            c = 1
            while l+c < n and nums[l] + c == nums[l+c]:
                c += 1
            if(c == 1): ans.append(str(nums[l]))    
            else: 
                ans.append(str(nums[l])+'->'+str(nums[l+c-1]))
            i = l+c
        return ans