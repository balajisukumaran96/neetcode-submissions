class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        def swap (nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= right:
            if nums[i] == 0:
                swap(nums, i, left)
                left += 1
            elif nums[i] == 2:
                swap(nums, i, right)
                right -= 1
                i -= 1 #we are moving i from left to right so i would know nums too its left is either (0,1), if it is 2 we swap with right and bring a new unknown value which needs to be inspected thats why i -= 1
        
            i += 1

