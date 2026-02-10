class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for left in range(n):
            even = set()
            odd = set()
            for right in range(left, n):
                if nums[right] % 2 == 0:
                    even.add(nums[right])
                else:
                    odd.add(nums[right])
                if abs(len(even) - len(odd)) > (n - right):
                    break
                if len(even) == len(odd):
                    max_len = max(max_len, right - left + 1)

        return max_len