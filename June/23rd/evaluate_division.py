# link: https://leetcode.com/problems/evaluate-division/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = {}
        for i in range(len(equations)):
            x = equations[i]
            adj.setdefault(x[0], {})[x[1]] = values[i]
            adj.setdefault(x[1], {})[x[0]] = 1.0/values[i]
        n = len(queries)
        ans = []
        v = 1
        def dfs(a, b):
            if a not in adj or b not in adj: return -1.0
            s = [(a,1.0)]
            v = set()
            while s:
                cur = s.pop()
                node, val = cur
                if node == b: return val
                v.add(node)
                for x in adj[node]:
                    if x not in v:
                        s.append((x, val * adj[node][x]))
            return -1.0
        for q in queries:
            ans.append(dfs(q[0], q[1]))
        return ans

