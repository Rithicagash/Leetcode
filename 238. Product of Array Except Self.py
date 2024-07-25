class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multi = 1
        zer = 0
        ans = []
        
        for i in nums:
            if i != 0:
                multi = multi * i
            else:
                zer+=1
        
        if zer >= 2:
            for i in range(len(nums)):
                ans.append(0)
        else:
            for i in range(len(nums)):
                if zer == 1 and nums[i] != 0:
                    ans.append(0)
                elif zer == 0:
                    ans.append(multi/nums[i])
                else:
                    ans.append(multi)
        return ans
