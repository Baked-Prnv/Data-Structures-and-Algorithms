"""53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
-----------------------------------------------------------------------------------------
Kadane's algorithm. taking two pointer approach
"""

class Solution():
    
    def maxSubArray(self, nums):
        maxSum = nums[0]
        currSum = 0

        for i in nums:
            if currSum<0:
                currSum=0
            currSum += i
            maxSum = max(maxSum, currSum)
        
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4] 
sol = Solution()
ans = sol.maxSubArray(nums)
print(ans)

nums = [1]
ans = sol.maxSubArray(nums)
print(ans)

nums = [5,4,-1,7,8]
ans = sol.maxSubArray(nums)
print(ans)