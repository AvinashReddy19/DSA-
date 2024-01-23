
#Optimal solution is KADANE'S ALGO
# BF:
def maxSubArray(nums):
        ans = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))


# Time Complexity: O(N^2)
# Space Complexity: O(1)

# OPTIMAL:


def maxSubArray(nums):
        sum = 0
        maxi= float("-inf")
        for i in range(len(nums)):
            sum+=nums[i]
            maxi=max(maxi,sum)
            if sum<0:
                sum=0
        return maxi


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
# Time Complexity: O(N)
# Space Complexity: O(1)