class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            total = 0
            while num:
                total += num % 10
                num //= 10
            num = total
        return num
