class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) ==1:
            return nums[0]

        maxAM = [0] * len(nums)
        maxAM[0] = nums[0]
        maxAM[1] = max(nums[1], maxAM[0])

        for i in range(2, len(nums)):
            maxAM[i] = max(nums[i]+maxAM[i-2], maxAM[i-1])
        
        return max(maxAM)
