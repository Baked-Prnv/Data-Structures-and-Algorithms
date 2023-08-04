"""75. Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Input: nums = [2,0,2,1,1,0]         Output: [0,0,1,1,2,2]
Input: nums = [2,0,1]               Output: [0,1,2]"""


class Solution():
    def sort(self, nums):
        l,r = 0,len(nums)-1
        i = 0

        while i<=r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
                r-=1
                i-=1                                #when 2 is swapped, i shoudn't be incremented 
            i+=1                                    #(swapped could be 0 and might skip in loop):edge case

        return nums
    

print(Solution().sort(nums = [2,0,2,1,1,0]))             #[0, 0, 1, 1, 2, 2]        

print(Solution().sort(nums = [2,0,1]))                   #[0, 1, 2]        