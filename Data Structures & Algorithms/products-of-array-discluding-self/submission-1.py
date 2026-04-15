class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, zero_count = 1 , 0 
        for i in nums:
            if i != 0:
                total *= i
            else: 
                zero_count += 1 
        if zero_count > 1 : return [0]*len(nums)


        result = [0] * len (nums)
        for i, num in enumerate (nums):
            if zero_count: 
                result[i] = 0 
                if num == 0:
                    result[i] = total
            else: 
                result[i]= total // num
        return result
        