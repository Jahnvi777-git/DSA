# link: https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return "0"
        frac = []
        if (numerator < 0) ^ (denominator < 0): frac.append("-")
        dividend = abs(numerator)
        divisor = abs(denominator)
        frac.append(str(dividend // divisor))
        rem = dividend%divisor
        if rem == 0:
            return "".join(frac)
        frac.append(".")
        hm = {}
        while rem != 0:
            if rem in hm:
                frac.insert(hm[rem], "(")
                frac.append(")")
                break
            hm[rem] = len(frac)
            rem = rem*10
            frac.append(str(rem // divisor))
            rem = rem%divisor
        return "".join(frac)
