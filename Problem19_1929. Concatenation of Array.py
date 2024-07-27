# 1929. Concatenation of Array Link: https://leetcode.com/problems/concatenation-of-array/description/

# Solution:

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(2):
            for j in range(len(nums)):
                x.append(nums[j])
        return x
