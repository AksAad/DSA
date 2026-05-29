class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_e = max(nums)
        for num in nums:
            min_e = min(min_e , sum(int(digit) for digit in str(num)))
        return min_e