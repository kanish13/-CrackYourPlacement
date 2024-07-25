# 169. Majority Element Link: https://leetcode.com/problems/majority-element/description/

# Solution:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=0
        c=0
        for i in nums:
            if c==0:
                maj=i
                c=1
            else:
                c=c+(1 if i==maj else -1)
        return maj
