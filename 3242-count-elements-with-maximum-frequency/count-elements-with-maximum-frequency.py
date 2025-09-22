class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = Counter(nums)
        max_frequency = max(n.values())
        total_count = sum(freq for freq in n.values() if freq == max_frequency)
        return total_count