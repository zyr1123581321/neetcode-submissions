class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = int(math.prod(nums))
        prod = [0 for j in range(len(nums))]

        for i, num in enumerate(nums):
            if num == 0:
                new_list = nums[:i] + nums[i+1:]
                prod[i] = int(math.prod(new_list))
            else:
                prod[i] = total // num
        return prod
                