class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_jump = 0
        for n in nums:
            if curr_jump < 0:
                return False
            elif n > curr_jump:
                curr_jump = n
            curr_jump -= 1
            
        return True