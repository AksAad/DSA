class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i = 0
        def checker(n:List[int]) -> bool:
            c1 = n[:k]
            c2 = n[k: ]
            if all(c1[i] < c1[i+1] for i in range(len(c1)-1)) and all(c2[i] < c2[i+1] for i in range(len(c2)-1)):
                return True
            else:
                return False
        while i <= len(nums) - 2*k:
            if checker(nums[i:i+2*k]) == True:
                return True
            i+=1
        return False