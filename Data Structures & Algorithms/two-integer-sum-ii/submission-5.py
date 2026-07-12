class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)

        while l < r:
            if numbers[l-1] + numbers[r-1] == target:
                return [l, r]
            if numbers[l-1] + numbers[r-1] < target:
                l += 1
            else:
                r -= 1
        return None