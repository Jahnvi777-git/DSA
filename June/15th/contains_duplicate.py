# link: https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = set()
        for i in nums:
            if i in l: return True
            l.add(i)
        return False
        