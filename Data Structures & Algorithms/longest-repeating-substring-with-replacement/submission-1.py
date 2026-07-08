class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        n = len(s)
        max_length = 0
        freq = dict()

        while right < n:
            freq[s[right]] = 1 + freq.get(s[right],0)

            maxf = max(freq.values())
            while (right - left + 1) - maxf > k:
                freq[s[left]] -= 1
                left += 1

            windowLen = right - left + 1
            max_length = max(max_length, windowLen)
            right += 1

        return max_length
