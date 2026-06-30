# link: https://leetcode.com/problems/ransom-note/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        f = [0] * 26
        for x in magazine:
            f[ord(x) - ord('a')] += 1
        for x in ransomNote:
            f[ord(x) - ord('a')] -= 1
            if f[ord(x) - ord('a')] < 0: return False
        return True
