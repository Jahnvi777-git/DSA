# link: https://leetcode.com/problems/can-place-flowers/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if n == 0: return True
        k = 0
        if l >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            k += 1
            flowerbed[0] = 1
        if l >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            k += 1
            flowerbed[-1] = 1
        if l == 1: return flowerbed[0] == 0 and n <= 1
        for i in range(1, l-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                k += 1
        return k >= n
