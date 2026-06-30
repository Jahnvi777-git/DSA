# link: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        nums = sorted(nums)
        if k%2 == 1:
            nums[0] = -nums[0]
        return sum(nums)
        
