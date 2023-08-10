"""1310. XOR Queries of a Subarray
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
Return an array answer where answer[i] is the answer to the ith query
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]             Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]            Output: [8,0,4,4]"""


class Solution():
    def XorQueries(self, arr, queries):
        n = len(arr)
        prefix = [0]*(n+1)                                          #as we need prefix[l-1] which could be [-1]

        for i in range(n):
            prefix[i+1] = prefix[i]^arr[i]

        res = []
        for l,r in queries:
            res.append(prefix[r+1]^prefix[l])                       #res = prefix[r]^prefix[l-1]

        return res
    

print(Solution().XorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))          #[2, 7, 14, 8]

print(Solution().XorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))         #[8, 0, 4, 4]