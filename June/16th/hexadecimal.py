# link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        n = len(s)
        m = len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                while j < m and s[i] != t[j]:
                    j += 1
        return i == n
            