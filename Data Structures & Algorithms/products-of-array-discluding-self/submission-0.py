class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        acc_mult = 1
        for i in range(n):
            acc_mult *= nums[i]
            prefix[i] = acc_mult

        suffix = [1] * n
        acc_mult = 1
        for i in range(n - 1, -1, -1):
            acc_mult *= nums[i]
            suffix[i] = acc_mult

        result = [suffix[1]] + [1]*(n - 2) + [prefix[-2]]
        for i in range(1, n-1):
            result[i] = prefix[i-1] * suffix[i+1]

        return result

        

        

        