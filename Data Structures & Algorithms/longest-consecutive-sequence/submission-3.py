class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return len(nums)

        result = 0
        num_set = set(nums)

        for num in num_set:
            if (num-1) not in num_set:
                current_length = 0
                current_num = num
                while current_num in num_set:
                    current_num += 1
                    current_length += 1
                if current_length > result:
                    result = current_length

        return result
