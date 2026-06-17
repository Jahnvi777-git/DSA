# link: https://leetcode.com/problems/random-pick-with-weight/description/?envType=problem-list-v2&envId=d5qblqpi 
import random, bisect

class Solution:

    def __init__(self, w: List[int]):
        self.ps = []
        t = 0
        for i in w:
            t += i
            self.ps.append(t)
        self.t = t

    def pickIndex(self) -> int:
        rand = random.randint(1, self.t)
        return bisect.bisect_left(self.ps, rand)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()