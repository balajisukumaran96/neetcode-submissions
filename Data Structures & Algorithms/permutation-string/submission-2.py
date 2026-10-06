class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
    
        if len(s1) > len(s2):
            return False
        
        hash_table1 = [0] * 26
        hash_table2 = [0] * 26
        
        for i in range(n):
            hash_table1[ord(s1[i])-ord('a')] += 1
        
        for right in range(m):
            hash_table2[ord(s2[right])- ord('a')] += 1

            if right >= n:
                left = right - n
                hash_table2[ord(s2[left]) - ord('a')] -= 1
            
            if right >= n - 1:
                if hash_table1 == hash_table2:
                    return True

        return False
             


        