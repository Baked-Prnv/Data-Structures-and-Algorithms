"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
---------------------------------------------------------------------------------------------------------------------------
using hashmap with hash function such hashmap[nums[i]]=i and by getting the compliment from the target and checking if it is present in hashmap"""

class Solution():
    def twoSum(self, nums, target):
        hashmap = {} 

        for i in range(len(nums)):
            compliment = target-nums[i]
            
            if compliment in hashmap and hashmap[compliment] != i:
                return [hashmap[compliment],i]
            
            hashmap[nums[i]] = i

nums = [2,7,11,15]
target = 9
sol = Solution()
ans = sol.twoSum(nums, target)
print(ans)

nums = [3,2,4]
target = 6
ans = sol.twoSum(nums, target)
print(ans)

nums = [3,3]
target = 6
ans = sol.twoSum(nums, target)
print(ans)