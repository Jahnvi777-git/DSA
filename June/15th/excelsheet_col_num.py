# link: https://leetcode.com/problems/excel-sheet-column-number/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord('A') + 1)

        return ans