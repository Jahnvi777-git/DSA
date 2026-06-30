# link: https://leetcode.com/problems/loud-and-rich/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        adj = [[] for _ in range(n)]
        for x in richer:
            adj[x[1]].append(x[0])
        res = [-1] * n

        def dfs(i):
            if res[i] >= 0: return res[i]
            res[i] = i
            for j in adj[i]:
                if quiet[res[i]] > quiet[dfs(j)]: res[i] = res[j]
            return res[i]
        for i in range(n): dfs(i)
        return res
