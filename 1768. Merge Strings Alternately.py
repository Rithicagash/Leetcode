class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a=len(word1)
        b=len(word2)
        ans=''
        for i in range(min(a,b)):
            ans += word1[i]
            ans += word2[i]
        ans += word1[b:] if a > b else word2[a:]
        return ans
        
        
        
