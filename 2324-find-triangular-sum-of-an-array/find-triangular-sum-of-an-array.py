class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i = 0
        newNums = []
        while i < len(nums) - 1:
            newNums.append((nums[i] + nums[i+1]) % 10)
            i+=1
        nums = newNums
        return self.triangularSum(nums)