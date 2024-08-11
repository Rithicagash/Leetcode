class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Set=set()
        
        n=len(nums)
        
        nums.sort()
        
        for i in range(n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        Set.add((nums[i],nums[j],nums[k],nums[l]))
                        k=k+1
                        l=l-1
                    
                    elif sum>target:
                        l=l-1
                    
                    else:
                        k=k+1
                        
        return [list(i) for i in Set]
                
