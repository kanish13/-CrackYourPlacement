class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pair = 0
        count = 0
        s = set(nums)
        for i in s:
            temp = nums.count(i)
            pair += temp // 2
            count += temp % 2
        return [pair, count]
