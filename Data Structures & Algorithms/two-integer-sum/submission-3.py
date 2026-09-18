class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        n = len(nums)

        for i in range(n):
            operand2 = target-nums[i]
            if operand2 in map:
                return [map[operand2], i]
            map[nums[i]] = i

        return None