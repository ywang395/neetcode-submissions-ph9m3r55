class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        clean = ""
        for ch in s: 
            if ch.isalnum(): 
                clean += ch.lower()
        for i in range(len(clean) // 2): 
            if clean[i] != clean [-(i + 1)]:
                return False 
        return True