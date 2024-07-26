class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for i in range(0,31):
            if n==(4**i):
                return True
