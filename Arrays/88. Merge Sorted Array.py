"""88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

class Solution():
    def merge(self,nums1,m,nums2,n):

        last = m+n-1
        while n>0 and m>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[last] = nums2[n-1]
                n-=1
            else:
                nums1[last] = nums1[m-1]
                m-=1
            last -= 1
        
        while n>0:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1

        return nums1
    
sol = Solution()
ans = sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
print(ans)                                                                      #[1, 2, 2, 3, 5, 6]

ans = sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
print(ans)                                                                      #[1]

ans = sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
print(ans)                                                                      #[1]

ans = sol.merge(nums1 = [1,2,3,5,6,7,0,0,0], m = 6, nums2 = [4,5,9], n = 3)
print(ans)                                                                      #[1, 2, 3, 4, 5, 5, 6, 7, 9]