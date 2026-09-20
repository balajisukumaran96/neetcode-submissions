class Solution:

    def merge(self, nums: List[int], start: int, mid: int, end: int) -> None:
        i, j, k = start, mid + 1, 0
        total_elements = end - start + 1
        merged_array = [0] * total_elements

        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                merged_array[k] = nums[i]
                i += 1
            else:
                merged_array[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            merged_array[k] = nums[i]
            i += 1
            k += 1

        while j <= end:
            merged_array[k] = nums[j]
            j += 1
            k += 1

        k = 0
        for idx in range(start, end + 1):
            nums[idx] = merged_array[k]
            k += 1

    def mergeSort(self, nums: List[int], start: int, end: int) -> None:
        if start < end:
            mid = start + (end - start) // 2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, 0, n - 1)
        return nums