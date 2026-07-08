class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        minHeap = []

        for num in num_count.keys():
            heapq.heappush(minHeap, (num_count[num], num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])

        return result