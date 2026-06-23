# link: https://leetcode.com/problems/combinations/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.f(1, n, k, [])
        return self.ans
    
    def f(self, i, n, k, p):
        if len(p) == k:
            self.ans.append(p[:])
            p = []
            return
        for num in range(i,n+1):
            p.append(num)
            self.f(num+1, n, k, p)
            p.pop()
        
