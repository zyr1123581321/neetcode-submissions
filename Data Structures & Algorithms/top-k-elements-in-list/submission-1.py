class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        descending_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return list(descending_dict)[:k]       