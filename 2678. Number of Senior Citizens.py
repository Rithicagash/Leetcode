class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for c in details:
            age=int(c[11]+c[12])
            if age>60:
                count+=1
        return count
        
