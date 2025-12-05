class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        a = sum(nums)
        if a%2 == 0:
            return len(nums) - 1
        else:
            return 0 
