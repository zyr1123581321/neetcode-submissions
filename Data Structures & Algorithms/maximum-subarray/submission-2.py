class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        maxS = float('-inf')

        for i in range(len(prefix)-1):
            for j in range(i+1, len(prefix)):
                sum = prefix[j] - prefix[i]
                maxS = max(sum, maxS)
        return maxS
