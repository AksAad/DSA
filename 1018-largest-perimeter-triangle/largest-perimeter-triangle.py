class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        triangle =[]
        #sum of any two sides is greater than the third side
        def checker(num1: int, num2: int, num3: int) -> bool:
            if(num1 + num2 > num3 and num2+num3 > num1 and num3+num1 > num2):
                return True
            else:
                return False
        if len(nums) == 3:
            if checker(nums[0], nums[1] , nums[2]) == True:
                return sum(nums)
            else:
                return 0
        else:
            nums.sort(reverse = True)
            while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
                nums.pop(0)            
            return 0 if len(nums) < 3 else sum(nums[:3])