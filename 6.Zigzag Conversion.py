class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1 or len(s) <= numRows:
            return s

        zigzag = [""] * numRows
        row = 0
        step = 1

        for char in s:
            zigzag[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        return "".join(zigzag)
            
