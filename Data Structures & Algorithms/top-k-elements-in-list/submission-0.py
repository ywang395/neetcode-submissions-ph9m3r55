class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        max_count = 0 
        for num in nums : 
            counts[num] = counts.get(num,0)+1;
            if counts[num] > max_count:
                max_count = counts[num]
        
        groups = []
        for num , count in counts.items():
            groups.append([count,num]) 
        groups.sort()
        
        result = []
        while len (result) < k:
            result.append(groups.pop()[1])
        return result
