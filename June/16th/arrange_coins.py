# link: https://leetcode.com/problems/arranging-coins/description/?envType=problem-list-v2&envId=d5qblqpi
import math

class Solution(object):
    def arrangeCoins(self, n):
        return int((math.sqrt(8 * n + 1) - 1) // 2)
    