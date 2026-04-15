class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t): 
            return False
        else:
            check = {}
            for word in s:
                check[word]= check.get(word, 0) + 1
            for word in t: 
                if word in check:
                    check[word] -= 1
            for word in check.values():
                if word != 0:
                    return False
            
        return True
            

        
            

        