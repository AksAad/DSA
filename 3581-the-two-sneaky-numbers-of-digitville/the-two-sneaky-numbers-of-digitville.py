class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        result = []
        for element, count in n.items():
            if count == 2:
                result.append(element)
        return result