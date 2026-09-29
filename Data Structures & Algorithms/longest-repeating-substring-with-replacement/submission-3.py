import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0] * 256
        left, right = 0, 0
        n = len(s)
        max_frequency = -1
        max_length = 0
        while right < n:
            char_count[ord(s[right])] += 1
            max_frequency = max(max_frequency, char_count[ord(s[right])])

            if (right - left + 1) - max_frequency > k:
                # 2 option for left if can be non frequent or frequent if non frequent the shrinked string will be valid the condition wont be violated but if it is frequent the condition will be violeted but we have one extra space and the result wont be affected like if we reduce tthe length max_frequency will also be reduced but the previous result would have already captured the correct result.
                char_count[ord(s[left])] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1 
        return max_length





