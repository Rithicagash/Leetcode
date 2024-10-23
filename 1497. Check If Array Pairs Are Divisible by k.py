class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        freq = [0] * k
        for i in range(len(arr)):
            freq[arr[i] % k] += 1

        if((freq[0]&1) == 1):   return False
        
        for i in range(1, k / 2 + 1):
            if(freq[i] != freq[k - i]):  return False
        
        return True
