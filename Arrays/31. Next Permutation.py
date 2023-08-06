"""31. Next Permutation
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.
Input: nums = [1,2,3]
Output: [1,3,2]
Input: nums = [3,2,1]
Output: [1,2,3]
Input: nums = [1,1,5]
Output: [1,5,1]
------------------------------------------------
The next permutation of the given list [0, 1, 3, 10, 9, 4, 2, 0] can be found using the following steps:
Start from the rightmost element and find the first pair of consecutive elements where the left element is smaller than the right element(3, 10).
Now, we need to find the smallest element to the right of 3 that is greater than 3(4). Swap the elements 3 and 4.
Reverse the sublist to the right of the swapped elements. In this case, it's [10, 9, 4, 2, 0], which becomes [0, 2, 4, 9, 10].
Putting it all together, the correct next permutation is: [0, 1, 4, 10, 9, 3, 2, 0]."""


class Solution():
    def nextPerm(self,nums):
        length = len(nums)

        if length<=2:                                           #edgeCase for 0,1,2 values
            return nums.reverse()
        
        pointer = length-2                                      #pointing at second last
        while pointer>=0 and nums[pointer]>=nums[pointer+1]:    
            pointer-=1
        
        if pointer<0:                                           #if the pointer goes out of bound ie., list is in desc order (4,3,2,1)
            return nums.reverse()                               #next perm is reverse(1,2,3,4)
        
        for i in range(length-1,pointer,-1):
            if nums[pointer]<nums[i]:
                nums[pointer],nums[i] = nums[i],nums[pointer]
                break
        
        # nums[pointer+1:] = nums[pointer+1:][::-1]             # to reverse 
        nums[pointer+1:] = reversed(nums[pointer+1:])


nums = [1,2,3]
Solution().nextPerm(nums)
print(nums)                                                     #[1, 3, 2]

nums = [3,2,1]
Solution().nextPerm(nums)
print(nums)                                                     #[1, 2, 3]

nums = [1,1,5]
Solution().nextPerm(nums)
print(nums)                                                     #[1, 5, 1]

nums = [0, 1, 3, 10, 9, 4, 2, 0]
Solution().nextPerm(nums)
print(nums)                                                     #[0, 1, 4, 0, 2, 3, 9, 10]
