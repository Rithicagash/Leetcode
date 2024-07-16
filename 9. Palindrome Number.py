class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        b = x
        reversed_x = 0
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        if reversed_x == b:
            return True
       

        
