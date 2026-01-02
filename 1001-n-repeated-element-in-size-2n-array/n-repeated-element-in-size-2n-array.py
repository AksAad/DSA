class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for num, freq in count.items():
            if freq == n // 2:
                return num