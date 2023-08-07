"""15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Input: nums = [0,1,1]
Output: []
Input: nums = [0,0,0]
Output: [[0,0,0]]"""


class Solution():
    def threeSum(self,nums):
        res=[]
        nums.sort()

        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:                      #to avoid duplicates in iteration
                continue

            l,r = i+1,len(nums)-1
            while l<r:
                currSum = num+nums[l]+nums[r]
                if currSum>0:
                    r-=1
                elif currSum<0:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:           #if the new nums is same as prev
                        l+=1

        return res
    
print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))                     #[[-1, -1, 2], [-1, 0, 1]]

print(Solution().threeSum(nums = [0,1,1]))                              #[]

print(Solution().threeSum(nums = [0,0,0]))                              #[[0, 0, 0]]