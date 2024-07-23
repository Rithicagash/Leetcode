class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            if "inf" in s.lower() or "nan" in s.lower():
                return False
            return True
        except:
            return False
