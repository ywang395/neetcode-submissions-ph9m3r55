class Solution:
    def maxArea(self, heights: List[int]) -> int: 

        i = 0  ## leftSide 
        k = len(heights) - 1  ## rightSide 
        area =  ( k - i ) * min (heights[i],heights[k])
        while i < k : 
            if heights[i] > heights[k]: 
                k -= 1 

            elif heights[i] < heights[k]:
                i += 1
            
            elif heights[i] == heights[k]:
                i += 1 
            
            new_area = ( k - i ) * min (heights[i],heights[k])
            if new_area > area: 
                area = new_area
            
        return area