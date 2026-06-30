# link: https://leetcode.com/problems/longest-palindrome/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        f = {}
        for x in s:
            if x not in f: f[x] = 1
            else: f[x] += 1
        o = 0
        t = 0
        for x in f.keys():
            if f[x]%2 == 1: 
                o += 1
                t += f[x] - 1
            else: t += f[x]
        if o >= 1: return t + 1
        return t
