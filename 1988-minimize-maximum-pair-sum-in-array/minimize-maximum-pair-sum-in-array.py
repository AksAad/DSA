class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_val = 0
        i = 0
        j = len(nums) - 1
        while i < j:
            max_val = max(max_val, nums[i]+nums[j])
            i+=1
            j-=1
        return max_val