class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0 
        i , k =0 , len(height) - 1 
        total_water = 0 ; 
        maxright , maxleft = height[k] , height[i]

        while i < k : 
            if maxleft < maxright :
                i += 1 
                maxleft = max (maxleft,height [i])
                total_water += maxleft - height [i]
            else: 
                k -= 1 
                maxright = max (maxright,height [k])
                total_water += maxright - height [k]
        return total_water


