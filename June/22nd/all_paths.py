# link: https://leetcode.com/problems/all-paths-from-source-to-target/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        used = [False for _ in range(n)]
        s = [0]
        ans = []
        used[0] = True
        def dfs(node, s, used):
            if node == n-1:
                ans.append(s)
                s = []
                return
            if not graph[node]: return
            for x in graph[node]:
                if not used[x]:
                    used[x] = True
                    dfs(x, s + [x], used)
                    used[x] = False
        dfs(0, s, used)
        return ans

