"""189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
------------------------------------------------------------------------------------------------
first rotating the whole array, then rotating the first k elements and other n-k elements.
"""

class Solution():

    def rotateArray(self, nums, k):
        k %= len(nums)

        def reverse(start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1

        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

        return nums

nums = [1,2,3,4,5,6,7]
k = 3    
sol = Solution()
ans = sol.rotateArray(nums,k)
print(ans)

nums = [-1,-100,3,99]
k = 2
ans = sol.rotateArray(nums,k)
print(ans)