class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0]
        sum = 0
        for num in nums:
            prefixSums.append(prefixSums[-1]+num)
            sum += num

        for i in range(len(nums)):
            if prefixSums[i] == (sum - prefixSums[i+1]):
                return i
        
        return -1
