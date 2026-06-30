# link: https://leetcode.com/problems/bulls-and-cows/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = {}
        a, b = 0, 0
        l = []
        for i in secret:
            if i in s:
                s[i] += 1
            else: s[i] = 1
        for i in range(len(secret)):
            if secret[i] == guess[i]: 
                a+=1
                if secret[i] in s: 
                    s[secret[i]] -= 1
                    if s[secret[i]] == 0: del s[secret[i]]
            else: l.append(i)
        for i in l:
            if guess[i] in s:
                b += 1
                s[guess[i]] -= 1
                if s[guess[i]] == 0: del s[guess[i]]
        return str(a) + 'A' + str(b) + 'B'
