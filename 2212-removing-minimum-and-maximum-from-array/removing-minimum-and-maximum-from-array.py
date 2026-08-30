class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        mn_idx = nums.index(min(nums))
        mx_idx = nums.index(max(nums))
        l = min(mn_idx, mx_idx)
        r = max(mn_idx, mx_idx)
        front = r + 1
        back = n - l
        both = (l + 1) + (n - r)
        return min(front, back, both)