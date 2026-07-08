class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        result = [0] * len(nums)

        temp = 1
        for i in range(len(nums)):
            prefix[i] = temp * nums[i]
            temp = prefix[i]

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = temp * nums[i]
            temp = suffix[i]
        
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right =  suffix[i+1] if i < len(nums)-1 else 1
            result[i] = left * right

        return result