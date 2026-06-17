# link: https://leetcode.com/problems/find-pivot-index/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = []
        t = 0
        for i in nums:
            t+=i
            ps.append(t)
        ss = []
        t = 0
        for i in nums[::-1]:
            t += i
            ss.append(t)
        for x in range(len(ps)):
            if ps[x] == ss[::-1][x]: return x
        return -1