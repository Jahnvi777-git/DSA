# link: https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(set(nums))
        if len(nums)>=3:
            return nums[-3] 
        else:
            return nums[-1]