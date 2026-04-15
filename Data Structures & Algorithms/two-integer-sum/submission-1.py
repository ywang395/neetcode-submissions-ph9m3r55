class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check= {} ## Dict of List 

        for i, num in enumerate(nums):
            if num in check:
                check[num].append(i)
            else:
                check[num] = [i]
        for x in nums: 
            complement = target - x 
            if complement in check:
                if nums.index(x) != check[complement][0]:
                    return [nums.index(x),check[complement][0]]
                else:
                    if len(check[complement]) > 1 : 
                        return [nums.index(x),check[complement][1]]
                



            
