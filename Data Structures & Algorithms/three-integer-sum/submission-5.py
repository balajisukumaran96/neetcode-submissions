class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numbers= nums
        result = []

        for i in range (len(numbers)-2):

            if i > 0 and numbers[i] == numbers [i-1]:
                continue

            left = i + 1
            right = len(numbers) - 1

            while left < right:
                current_sum = numbers[i] + numbers[left] + numbers[right]

                if current_sum == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left -1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right +1]:
                        right -= 1

                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return result
                
        