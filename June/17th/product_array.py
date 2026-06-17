# link: https://leetcode.com/problems/product-of-array-except-self/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        res = [0] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]

        return res