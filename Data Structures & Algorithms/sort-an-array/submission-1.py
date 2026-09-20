class Solution:

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        mergeArray = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mergeArray.append(left[i])
                i += 1
            else:
                mergeArray.append(right[j])
                j += 1
        mergeArray.extend(left[i:])
        mergeArray.extend(right[j:])
        return mergeArray
        
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)