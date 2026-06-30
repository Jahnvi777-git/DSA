# link: https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 10: return []
        d = {}
        for i in range(n-9): 
            ss = s[i:i+10]
            if ss in d: d[ss] += 1
            else: d[ss] = 1
        ans = []
        for x in d:
            if d[x] > 1: ans.append(x)
        return ans
