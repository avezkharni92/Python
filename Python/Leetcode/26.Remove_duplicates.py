class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
    
        # The length of the unique elements list
        return nums[:i+1]
        
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))

def remove_duplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    
    # Return only the unique part of the array
    return arr[:i+1]

arr = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]


