# link: https://leetcode.com/problems/restore-ip-addresses/description/?envType=problem-list-v2&envId=d5qblqpi
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        add = ''
        n = len(s)
        def f(i, add, part):
            if part > 4:
                if check_full(add):
                    ans.append(add)
                    add = ''
                return 
           
            for j in range(i, n):
                if part == 4:
                    f(j+1, add + s[j:], part+1)
                    return
                else:
                    a = s[i:j+1]
                    if check(a):
                        f(j+1, add + a + '.', part+1)
        
        def check(a):
            if not a: return False
            f = a[0] == '0' 
            return int(a) <= 255 and ((f and len(a) == 1) or (not f and int(a) > 0))

        def check_full(s):
            s = s.split('.')
            f = True
            for x in s:
                f = f and check(x)
            return f

        f(0, '', 1)
        return ans
