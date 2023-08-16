"""41. First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
Input: nums = [1,2,0]       Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Input: nums = [3,4,-1,1]    Output: 2
Explanation: 1 is in the array but 2 is missing.
Input: nums = [7,8,9,11,12] Output: 1
Explanation: The smallest positive integer 1 is missing.
-------------------------------------------------------------------------------------------
we have to find the smallest +ve num that is not in nums """

class Solution():
    def firstMissingPositive1(self,nums):                            #brute-force soln which will give TLE for larger value of nums
        if len(nums)>1:
            for i in range(1,len(nums)+2):
                if i not in nums:
                    return i            
        else:
            if nums[0]==1:
                return 2
            return 1
    
    def firstMissingPositive2(self,nums):                           #using sorting alogorithm
        nums.sort()
        smallest_missing=1
        
        for num in nums:
            if num == smallest_missing:
                smallest_missing+=1
            elif num>smallest_missing:
                return smallest_missing
            
        return smallest_missing

    def firstMissingPositive(self,nums):                
        for i in range(len(nums)):                          #making all the -ve nums to 0
            if nums[i]<0:
                nums[i]=0

        for i in range(len(nums)):                          #now only +ve nums and 0 are in nums
            val = abs(nums[i])                              
            if 1<=val<=len(nums):                           #if its in range[1,len(nums)+1]
                if nums[val-1]>0:                           #making its index value -ve i.e., 
                    nums[val-1] *= -1                       #if 1 is there then making 0 index -ve 
                elif nums[val-1]==0:                        #if 0 then making it to -(len(nums)+1)
                    nums[val-1] = -1 * (len(nums)+1)

        for i in range(1, len(nums)+1):                     #now iterating from [1,len(nums)] if its +ve then return i
            if nums[i-1]>=0:
                return i
        
        return len(nums)+1                                  #if the array is [1,len(nums)] then returning the next ele


print(Solution().firstMissingPositive(nums = [1]))                  #2
print(Solution().firstMissingPositive(nums = [2,1]))                #3
print(Solution().firstMissingPositive(nums = [1,2,0]))              #3
print(Solution().firstMissingPositive(nums = [3,4,-1,1]))           #2
print(Solution().firstMissingPositive(nums = [7,8,9,11,12]))        #1