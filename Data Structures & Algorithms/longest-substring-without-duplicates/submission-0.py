class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0
        n = len(s)
        longest_substring = 0
        word_set = set()

        while right < n:
            while s[right] in word_set:
                left_char = s[left]
                word_set.remove(left_char)
                left += 1
            word_set.add(s[right])
            longest_substring = max(longest_substring, len(word_set))
            right += 1
        
        return longest_substring
