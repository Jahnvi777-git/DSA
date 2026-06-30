# link: https://leetcode.com/problems/word-pattern/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        hm = {}
        rhm = {}
        l = s.split()
        n = len(l)
        m = len(pattern)
        if n != m: return False
        for i in range(n):
            c = pattern[i]
            if c not in hm and l[i] not in rhm: 
                hm[c] = l[i]
                rhm[l[i]] = c
            else:
                if c in hm and hm[c] == l[i] and l[i] in rhm and rhm[l[i]] == c: pass
                else: return False
        return True
