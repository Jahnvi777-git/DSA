# link: https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution:
    def findLHS(self, nums):
        frequency_map = Counter(nums)
        max_length = 0

        for num in frequency_map:
            if num + 1 in frequency_map:
                current_length = frequency_map[num] + frequency_map[num + 1]
                max_length = max(max_length, current_length)

        return max_length