# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)[::-1]
        length = len(num)
        outst=""
        for i in range(length):
            temp = int(num[i])
            if temp <= 3:
                outst = self.upToThree(temp,i) + outst
            elif temp == 4:
                outst = self.fourDet(i) + outst
            elif temp == 5:
                outst = self.fiveDet(i) + outst
            elif temp < 9:
                outst = self.fiveDet(i) + self.upToThree(temp-5,i) + outst
            else:
                outst = self.nineDet(i) + outst
        return outst
                
    
    def nineDet(self, dec: int) -> str:
        switch ={
            0: "IX", #9
            1: "XC", #90
            2: "CM", #900
        }
        return switch.get(dec,"")
    
    def fourDet(self, dec: int) -> str:
        switch = {
            0: "IV", #4
            1: "XL", #40
            2: "CD", #400
        }
        return switch.get(dec, "")
    
    def upToThree(self, num: int, dec: int) -> str:
        switch = {
            0: "I",
            1: "X",
            2: "C",
            3: "M",
        }
        return switch.get(dec,"")*num
    
    def fiveDet(self, dec: int) -> str:
        switch = {
            0: "V",
            1: "L",
            2: "D",
        }
        return switch.get(dec,"")
                