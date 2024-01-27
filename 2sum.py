# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    nums.sort()
    low=0
    high=len(nums)-1
    while low<high:
        if nums[low]+nums[high]==target:
            return [low,high]
        elif nums[low]+nums[high]>target:
            high-=1
        else:
            low+=1
    return [-1,-1]

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
# Time Complexity: O(N)
