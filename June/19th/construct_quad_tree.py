# link: https://leetcode.com/problems/construct-quad-tree/description/?envType=problem-list-v2&envId=d5qblqpi
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.f(grid, 0, 0, len(grid))

    def f(self, grid, x, y, l):
        is0 = False
        is1 = False
        for i in range(l):
            for j in range(l):
                if grid[x+i][y+j] == 1: is1 = True
                else: is0 = True
        if is0 and not is1:
            root = Node( 0, True, None, None, None, None)
        elif is1 and not is0:
            root = Node( 1, True, None, None, None, None)
        else:
            root = Node()
            root.isLeaf = False
            root.val = 0
            root.topLeft = self.f(grid, x, y, l//2)
            root.topRight = self.f(grid, x, y+(l//2), l//2)
            root.bottomLeft = self.f(grid, x+(l//2), y, l//2)
            root.bottomRight = self.f(grid, x+(l//2), y+(l//2), l//2)
        return root
