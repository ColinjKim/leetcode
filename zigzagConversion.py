#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s==None or len(s)==0:
            return s
        if numRows <= 1:
            return s
        strArr = [""] * numRows
        line = 0
        position = 1
        output = ""
        for i in range(len(s)):
            strArr[line] += s[i]
            line += position
            if line == numRows -1 or line == 0:
                position *= -1
        for i in range(numRows):
            # print(strArr[i], end="")
            output += strArr[i]
        return output