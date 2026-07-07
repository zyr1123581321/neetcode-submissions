class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}

        for i, n in enumerate(nums):
            if n in values:
                return True
            else:
                values[n] = i
        return False