# link: https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse = True)
        print(nums)
        def check(a,b,c):
            return (a+b > c and a+c > b and b+c > a)
        for i in range(len(nums)-2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if check(a,b,c): return a+b+c
        return 0
        
