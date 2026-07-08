class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        char_count = [0] * 26

        for a,b in zip(s,t):
            char_count[ord(a) - ord('a')] = char_count[ord(a) - ord('a')] + 1
            char_count[ord(b) - ord('a')] = char_count[ord(b) - ord('a')] - 1

        total = sum(char_count)
        
        

        return all(count == 0 for count in char_count)
            
            



