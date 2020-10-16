# https://leetcode.com/problems/container-with-most-water/submissions/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        L = 0
        R = len(height)-1
        tempMax = 0
        while (L<R):
            left = height[L]
            right = height[R]
            w = R-L
            if left<right:
                tempMax = left * w
                L+=1
            else:
                tempMax = right*w
                R-=1
            if tempMax > curMax:
                curMax = tempMax
        return curMax
 