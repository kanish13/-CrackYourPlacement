class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_indices = [i for i in range(1, len(nums), 2)]
        even_indices = [i for i in range(0, len(nums), 2)]
        odd_values = sorted([nums[i] for i in odd_indices], reverse=True)
        even_values = sorted([nums[i] for i in even_indices])
        for i, idx in enumerate(odd_indices):
            nums[idx] = odd_values[i]
        for i, idx in enumerate(even_indices):
            nums[idx] = even_values[i]
        return nums
