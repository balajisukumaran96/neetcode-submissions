
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        
        for i in range(len(nums)):
            current = nums[i]
            remaining = target - current;

            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[current] = i

        return [] 