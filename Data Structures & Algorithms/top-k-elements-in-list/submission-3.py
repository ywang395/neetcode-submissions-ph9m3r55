class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [] 
        result = []
        max_value = 0
        for num in nums: 
            count[num] = count.get(num,0)+1
        
        for key,value in count.items():
            #[ 3,2,1 ]
            frequencies.append([value,key])
            
            # { 1:3 , 2:2 , 3:1 } k = 2 
            # { 3:1 , 3:2 , 1:3 } swap the key and value 
        frequencies.sort()
        
        i = 0
        while len(result) < k :
            result.append(frequencies.pop()[1])

        return result