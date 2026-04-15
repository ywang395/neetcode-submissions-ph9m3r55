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
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}
        for string in strs: 
            if len(string) in group: 
                found = False
                nthKey = group[len(string)]
                for element in nthKey:
                    if self.isAnagram(element[0],string):
                        element.append(string)
                        found = True
                if found == False :
                    nthKey.append([string])

            else:    
                group[len(string)] = [[string]]
        result = []
        for element in group.values():
            result += element
        return result
                
                
            
            