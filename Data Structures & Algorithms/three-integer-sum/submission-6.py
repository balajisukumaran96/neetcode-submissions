class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        result=[]
        while i < n-2:
            if i > 0 and nums[i] == nums[i - 1]:
                i+=1
                continue

            if nums[i] > 0:
                break

            left = i+1
            right = n-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

            i+=1
        return result