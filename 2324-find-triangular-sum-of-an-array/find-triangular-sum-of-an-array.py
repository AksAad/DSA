class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums) - 1
        #to get the row of a pascals triangle then to multiply it with nums and add it to then take the modulus to get the solution
        if n < 0:
            return []
        row = [1]  
        for k in range(1, n + 1):
            next_element = (row[-1] * (n - k + 1)) // k
            row.append(next_element)
        l = 0
        newNums = []
        while l < len(nums):
            newNums.append(nums[l] * row[l])
            l+=1
        return sum(newNums) % 10 