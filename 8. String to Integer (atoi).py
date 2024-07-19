class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        ans = 0
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1
            if sign == 1 and ans >= 2**31:
                return 2**31 - 1
            if sign == -1 and ans > 2**31:
                return -2**31
        
        return sign * ans
