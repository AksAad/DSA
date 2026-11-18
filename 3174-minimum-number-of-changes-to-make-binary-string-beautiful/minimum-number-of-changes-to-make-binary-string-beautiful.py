class Solution:
    def minChanges(self, s: str) -> int:
        nums = [int(x) for x in s]
        total_change = 0
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i+1]:
                total_change += 1
        return total_change