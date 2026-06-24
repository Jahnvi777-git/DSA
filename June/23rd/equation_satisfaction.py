# link: https://leetcode.com/problems/find-the-town-judge/description/?envType=problem-list-v2&envId=d5qblqpi
class UnionFind:
    def __init__(self):
        self.parent = list(range(26))
    
    def find(self, x):
        if x!= self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px!= py:
            self.parent[px] = py
            return True
        return False

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for a, e, _, b in equations:
            if e == '=':
                uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        for a, e, _, b in equations:
            if e == '!':
                if uf.find(ord(a) - ord('a')) == uf.find(ord(b) - ord('a')):
                    return False
        return True
