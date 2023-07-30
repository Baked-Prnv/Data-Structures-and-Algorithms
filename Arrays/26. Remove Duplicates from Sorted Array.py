"""26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums. Return k.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
------------------------------------------------------------------------------------------------------------------------------------------
Using the two pointer approach to find the unique elements and shifting it to the start. since 0th element is unique, 
so starting l,r from 1 and since array is sorted, with r increasing till last and comparing if the previous element is not same 
and assigning it to lth element and incrementing l by 1 """

class Solution():
    
    def removeDuplicates(self, nums):
        l=1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1

        for i in range(l,len(nums)):    # Not Needed
            nums[i] = "_"

        return l,nums
    

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
ans = sol.removeDuplicates(nums)
print(ans)