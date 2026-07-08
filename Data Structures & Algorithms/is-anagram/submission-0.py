class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        map = {}

        for letter in s:
            if letter in map:
                map[letter] = map[letter] + 1
            else:
                map[letter] = 1

        for letter in t:
            if letter in map:
                map[letter] = map[letter] - 1
            else:
                return False

        for value in map.values():
            if value != 0:
                return False

        return True

            
            



