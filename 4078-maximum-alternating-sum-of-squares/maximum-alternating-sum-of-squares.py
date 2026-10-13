class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        squares = sorted([x*x for x in nums])
        if n%2==0:
            return  sum(squares[(n//2):]) - sum(squares[0:n//2])
        else:
            return sum(squares[(n//2):]) - sum(squares[0:(n//2)])