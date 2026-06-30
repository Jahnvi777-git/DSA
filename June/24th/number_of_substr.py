# link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = {}
        l, r, t, ans, n = 0, 0, 0, 0, len(s)
        while r < n:
            ss[s[r]] = ss.get(s[r], 0)+1
            while l <= r and len(ss) == 3:
                ans += n-r
                ss[s[l]] -= 1
                if(ss[s[l]] == 0): del ss[s[l]]
                l += 1
            r += 1
        return ans
