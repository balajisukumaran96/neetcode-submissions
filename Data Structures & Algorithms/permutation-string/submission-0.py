class Solution:
    def validator(self, s1: List, s2: List) -> bool:
        for i in range(26):
            if s1[i] != s2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        m = len(s2)
        hash_table1 = [0] * 26
        hash_table2 = [0] * 26
        left, right = 0, n-1

        for i in range(n):
            hash_table1[ord(s1[i])-ord('a')] += 1
        
        for i in range(n):
            hash_table2[ord(s2[i])-ord('a')] += 1
        
        if self.validator(hash_table1, hash_table2):
            return True
        
        while right < m-1:
            hash_table2[ord(s2[left])-ord('a')] -= 1
            left+=1
            right+=1
            hash_table2[ord(s2[right])-ord('a')] += 1
            if self.validator(hash_table1, hash_table2):
                return True

        
        return False
             


        