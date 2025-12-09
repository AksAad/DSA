class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count = 0
        before = defaultdict(int)
        after = defaultdict(int)
        for num in nums:
            after[num] += 1
        for num in nums:
            after[num] -= 1
            count = (count + (before[num * 2] * after[num * 2])) % 1000000007
            before[num] += 1
        return count