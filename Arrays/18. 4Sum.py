"""18. 4Sum
"""


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        return self.kSum(nums,target,4,0)
    
    def kSum(self, nums, target, k, start):
        if k!=2:
            all_result = []
            
            for i in range(start,len(nums)-k+1):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                
                sub_results = self.kSum(nums,target-nums[i],k-1,i+1)
                
                for sub_result in sub_results:
                    all_result.append([nums[i]]+sub_result)
            
            return all_result

        l,r = start,len(nums)-1
        res = []
        while l<r:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                res.append([nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
                    
        return res
    
print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))               #[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

print(Solution().fourSum(nums = [2,2,2,2,2], target = 8))              #[]