"""128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
-------------------------------------------
Create a HashSet of unique numbers from the array.
Initialize longest to track the maximum sequence length.
Iterate: For each number: Check Smaller: If no smaller neighbor, start a sequence. Count sequence length by checking larger neighbors.
Update Longest: Keep track of the longest sequence.
"""


class Solution():
    def longestConsecutive(self, nums):
        hashSet = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in hashSet:                # making sure its the smallest of any sequence present
                length = 0
                
                while num+length in hashSet:
                    length+=1

                longest = max(longest,length)

        return longest
    

print(Solution().longestConsecutive(nums = [100,4,200,1,3,2]))      #4

print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))      #9