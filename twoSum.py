#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for x in range(len(nums)):
            nums_dict[nums[x]] = x
        for x in range(len(nums)):
            compliment = target-nums[x]
            if compliment in nums_dict:
                check = nums_dict[compliment]
                if x!=check:
                    return[x,check]


