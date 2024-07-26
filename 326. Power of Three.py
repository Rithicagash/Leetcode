class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0,31):
            if n==(3**i):
                return True
