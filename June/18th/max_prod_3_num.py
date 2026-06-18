# link: https://leetcode.com/problems/maximum-product-of-three-numbers/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])