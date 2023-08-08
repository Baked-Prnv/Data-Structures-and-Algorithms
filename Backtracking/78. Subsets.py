"""78. Subsets
Given an integer array nums of unique elements, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Input: nums = [0]
Output: [[],[0]]"""


class Solution():
    def subset(self,nums):
        res = []
        subset = []

        def dfs(i):
            #base case
            if i>=len(nums):
                res.append(subset[:])
                return
            
            #desicion to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #desicion NOT to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
    

print(Solution().subset(nums = [1,2,3]))                    #[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

print(Solution().subset(nums = [0]))                        #[[0], []]