class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for num in nums:
            if (num + 1) not in num_set:
                count = 1
                current = num
                while (current-1) in num_set:
                    current = current-1
                    count += 1
                max_count = max(max_count,count)
        
        return max_count