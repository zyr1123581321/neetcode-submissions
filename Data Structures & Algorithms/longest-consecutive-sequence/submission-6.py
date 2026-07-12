class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_c = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                count = 1
                value = num +1
                while value in set_nums:
                    value += 1
                    count += 1    
                    
                max_c = max(max_c, count)
        return max_c