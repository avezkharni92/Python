class Solution:
    def maxProduct(self, nums):
        max_product = 0
        for i in range(len(nums)):
            for j in range((i+1), len(nums)):
                arr_product = (nums[i]-1) * (nums[j]-1)
                if arr_product > max_product:
                    max_product = arr_product
        return max_product


nums = [3,4,5,2]
solution = Solution()
max_pr = solution.maxProduct(nums)
print(max_pr)


