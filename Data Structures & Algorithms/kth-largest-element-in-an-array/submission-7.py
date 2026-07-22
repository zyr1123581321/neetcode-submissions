import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heappush(min_heap, nums[0])

        for i in range(1, len(nums)):
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]