class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax*n
            curMax = max(temp, n*curMin, n)
            curMin = min(temp, n*curMin, n)
            result = max(result, curMax)
            
        return result
