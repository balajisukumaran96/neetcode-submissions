class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = [-1] * 256
        left, right = 0, 0
        n = len(s)
        result = 0

        while (right < n):
            if left <= char_index[ord(s[right])]:
                left = char_index[ord(s[right])] + 1
            
            char_index[ord(s[right])] = right
            
            current_length = right - left + 1
            if current_length > result:
                result = current_length
            right += 1
        return result

