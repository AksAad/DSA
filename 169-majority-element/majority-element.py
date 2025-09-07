class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = Counter(nums)
        return temp.most_common(1)[0][0]