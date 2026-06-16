# link: https://leetcode.com/problems/gray-code/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]