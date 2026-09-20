class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        current = nums[0]

        for num in nums:
            if vote == 0:
                current = num
            if num == current:
                vote += 1
            else:
                vote -= 1

        return current