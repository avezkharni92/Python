#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return[i, j]


# Create an instance of the class
# sol = Solution()

# # Call the method with sample input
# result = sol.twoSum([2, 7, 11, 15], )

# # Print the result
# print(result)

# @lc code=end

