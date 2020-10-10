#https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s)==0:
            return ""
        s2 = self.addBoundaries(s)
        p = [0]*len(s2)
        c=r=m=n=0
        
        for i in range(len(s2)):
            if i>r:
                p[i] = 0
                m = i-1
                n = i+1
            else:
                i2 = c*2-i
                if p[i2] < (r-i-1):
                    p[i] = p[i2]
                    m = -1
                else:
                    p[i] = r-i
                    n = r+1
                    m=i*2-n
            while m>=0 and n<len(s2) and s2[m]==s2[n]:
                p[i] += 1
                m -= 1
                n += 1
            if (i+p[i])>r:
                c = i
                r = i+p[i]
        leng=c=0
        for i in range(len(s2)):
            if leng<p[i]:
                leng = p[i]
                c = i
        ss = s2[c-leng:c+leng+1]
        return self.removeBoundaries(ss)
    
    def addBoundaries(self, s:str) -> str:
        s2 = ""
        for c in s:
            s2+="|"+c
        s2+="|"
        return s2
    def removeBoundaries(self, s:str) -> str:
        return s.replace("|","")
            
