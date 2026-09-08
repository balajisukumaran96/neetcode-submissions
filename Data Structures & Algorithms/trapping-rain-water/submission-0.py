class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_left = float('-inf')
        max_right = float('-inf')
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    current_height = max_left - height[left]
                    total_water += current_height
                left += 1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    current_height = max_right - height[right]
                    total_water += current_height
                right -= 1
        
        return total_water
