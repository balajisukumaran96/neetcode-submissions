class Solution:

    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        start = left

        first_half = self.binary_search(nums, 0, start - 1, target)

        return first_half if first_half != -1 else self.binary_search(nums, start, len(nums) - 1, target)