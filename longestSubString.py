#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxlen = 0 #maximum length
        start = 0 #starting index
        pos = {} #dictionary to check repeating
        pos[s[0]] = 0
        for i in range(1,len(s)):
            if s[i] in pos:
                if pos[s[i]] >= start:
                    curlen = i - start
                    if maxlen < curlen:
                        maxlen = curlen
                    start = pos[s[i]] + 1
            pos[s[i]] = i
        if maxlen < len(s) - start:
            maxlen = len(s) -start
        return maxlen
    