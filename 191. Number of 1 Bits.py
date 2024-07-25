class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        set_bit_count = 0
        while n != 0:
            n &= (n - 1)
            set_bit_count += 1
        return set_bit_count
