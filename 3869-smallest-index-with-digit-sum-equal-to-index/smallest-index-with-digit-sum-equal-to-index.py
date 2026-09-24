class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            digit_sum = sum(int(digit) for digit in str(nums[i]))
            if i == digit_sum:
                return i
        return -1