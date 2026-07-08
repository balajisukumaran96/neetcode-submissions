class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")
        n = len(heights)
        left, right = 0, n - 1

        while left < right:
            current_area = (right - left) * min(heights[left],heights[right])
            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area   
        