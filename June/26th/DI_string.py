# link: https://leetcode.com/problems/di-string-match/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        low, high = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans
