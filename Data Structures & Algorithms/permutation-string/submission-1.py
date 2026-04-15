class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len (s1): 
            return False 
        count = {}
        for word in s1:
            count[word] = count.get(word, 0) + 1

        for l in range(len(s2)):
            count_s2 , curr = {} , 0 
            for r in range (l , len(s2)):
                count_s2 [s2[r]] = count_s2.get(s2[r], 0) + 1 
                if count.get(s2[r],0) < count_s2[s2[r]]:
                    break
                if count.get(s2[r], 0) == count_s2[s2[r]]:
                    curr += 1 
                if curr == len(count):
                    return True 
        return False