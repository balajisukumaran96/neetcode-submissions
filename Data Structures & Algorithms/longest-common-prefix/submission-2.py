class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n < 2:
            return strs[0]
        
        strs.sort(key=len)
        m = len(strs[0])
        result = []
        
        for i in range(m):
            current_char = strs[0][i]
            for j in range(1,n):
                if current_char != strs[j][i]:
                    return "".join(result)
            result.append(current_char)
            
        return "".join(result)