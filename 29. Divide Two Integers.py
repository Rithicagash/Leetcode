class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647  # Return the maximum value for a 32-bit signed integer


        if dividend<0 and divisor<0:
            a=int(dividend//divisor)
            return a
        
        elif dividend<0 or divisor<0:
            a=int(abs(dividend)//abs(divisor))*(-1)
            return a
       
        else:
            a=int(dividend//divisor)
            return a
