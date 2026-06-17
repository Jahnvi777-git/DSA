# link: https://leetcode.com/problems/continuous-subarray-sum/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        t = 0
        ps = {0: -1}
        for i in range(len(nums)):
            t += nums[i]
            if t%k in ps:
                if i - ps[t%k] >= 2: return True
            else: ps[t%k] = i
        return False



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_idx = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            rem = total % k

            if rem in rem_idx:
                if i - rem_idx[rem] >= 2:
                    return True
            else:
                rem_idx[rem] = i

        return False